import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import datetime
import requests
import json
import time
import pprint
import click
import config

##############################################
##              DO NOT CHANGE               ##
##############################################
base = 'https://reddwerks.zendesk.com/api/v2'


##############################################
##                FUNCTIONS                 ##
##############################################

def email_csv(filepath, to_addr):
    msg = MIMEMultipart()
    msg['From'] = 
    msg['To'] = to_addr
    msg['Subject'] = "Zentime"
    body = "Time CSV is attached "
    msg.attach(MIMEText(body, 'plain'))
    filename = "zentickets.csv"
    attachment = open("./zentickets.csv", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= {}".format(filename))
    msg.attach(part)
    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(from_addr, email_pass)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()


def get_seconds_from_days(days):
    return 86400 * days

def get_ticket_details(ticket_number):
    ticket_url = "{}/tickets/{}.json".format(base, ticket_number)
    response = requests.get(ticket_url, auth=(user, token))
    data = response.json()
    subject = ''
    ticket_type = ''
    customer_site = ''
    system = ''
    try:
        subject = data['ticket']['subject']
        ticket_type =  data['ticket']['type']
        #print data['ticket']['field you are trying to find']  #used for checking field IDs
        for fields in data['ticket']['custom_fields']:
            if fields['id'] == 30727457:
                customer_site = fields['value']
            if fields['id'] == 30770258:
                system = fields['value']
        return subject, ticket_type, customer_site, system
    except KeyError as e:
        print "pass"
        return subject, ticket_type, customer_site, system


def get_users(user_emails):
    url = '{}/users.json'.format(base)
    response = requests.get(url, auth=(user, token))
    data = response.json()
    users = {}
    for single_user in data['users']:
        if single_user['email'] in user_emails:
            users[single_user['id']] = single_user['email']
    return users


@click.command()
@click.option('--user_list', default=user_defined_list)
@click.option('--days', '-n', default=default_days)
def get_csv(user_list, days):
    """Grab timesheets from zendesk."""
    users = get_users(user_list)
    seconds_less = int(get_seconds_from_days(days))
    event_url = '{}/incremental/ticket_events.json?per_page=100&start_time={}&end_time={}'.format(base, int(time.time())-seconds_less, int(time.time())-360)
    print event_url
    try:
        csv = open("zentickets.csv", 'w')
        csv.write("ticket number, type, subject, site, system, worklog\n")
        check_stamp = ""
        while event_url is not None:
            response = requests.get(event_url, auth=(user, token))
            data = response.json()
            event_url = data['next_page']
            print event_url
            for ticket_event in data['ticket_events']:
                for child in ticket_event['child_events']:
                    if 'custom_ticket_fields' in child:
                        if '28302838' in child['custom_ticket_fields']:
                            timestamp = ticket_event['timestamp']
                            update_stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                            ticket_number = ticket_event['ticket_id']
                            updater_id = ticket_event['updater_id']
                            time_spent = child['custom_ticket_fields']['28302838']
                            if update_stamp == check_stamp:
                                event_url = None
                            else:
                                if time_spent == 0:
                                    pass
                                else:
                                    subject, ticket_type, customer_site, system = get_ticket_details(ticket_number)
                                    if not subject:
                                        print "No Subject"      
                                    else:
                                        check_stamp = update_stamp
                                        csv.write("{}, {}, {}, {}, {}, {};{};{}\n".format(ticket_number, ticket_type, subject, customer_site, system, update_stamp, users[updater_id], time_spent))
            time.sleep(6)
        csv.close()
        email_csv("./zentickets.csv", admin_email)
        print "CSV Generated."
    except (KeyError) as error:
        print "ERROR: {}".format(error)
        raise
if __name__ == '__main__':
    print "Starting Time.py"
    get_csv()
    print "Email sent, time.py complete"
    quit()
