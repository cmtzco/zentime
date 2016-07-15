##############################################
##              CONFIG BLOCK                ##
##############################################
# @string token - API Token
# @string user - This is found in Zendesk under Admin > Channels > API, Commonly your login_email/token
# @list user_defined_list - List of emails comma delimeted with the users you need to pull time from
# @string admin_email - Email of the person that will recieve the JIRA importable CSV
# @int default_days - Number of days to pull time for
# @string from_addr - Email that will be set up to send email via SMTP
# @string smtp_server - Hostname to send email from
# @string password - Password to the email that this will be sent from

token = 'TOKEN'
user = 'APIUSER/token'
user_defined_list = ['useremail@company.com', 'useremail2@company.com']
admin_email = "user@email.com"
default_days = 7
from_addr = "user@company.com"
smtp_server = 'mail.server.net'
email_pass = 'password'
