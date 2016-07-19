# Zentime


### Easily export time from Zendesk to import to JIRA


-  [Installation](https://github.com/cmtzco/zentime#installation "Installation")
-  [Configuration](https://github.com/cmtzco/zentime#configuration "Configuration")
-  [Usage](https://github.com/cmtzco/zentime#usage "Usage")


### Installation

Commands to run to install zentime requirements

    sudo ./install.sh

[Back to top](https://github.com/cmtzco/zentime#zentime)


### Configuration

In the config.py file you will see all the variables that need to be set in order for this 
to work with your Zendesk account.  Be sure that you have Admin access to your Zendesk 
instance if not you will not be able to proceed with getting a token on your own.  

The token will be generated in the API screen in the admin settings. 

    token = "CAVmMl1kaoRfky3VcH54kvAJ1PTI"

The user is the email account you logged into Zendesk with.  This must be an admin account 
in order for this to work. 

    user = "user@company.com"

The user defined list is a list of all the emails of all the users that you are trying to 
pull time for.  This is specified in a comma seperated list and is enclosed by the [] 
characters.  All emails must be within single or double quotes.

    user_defined_list = ['user1@company.com', 'user2@company.com']

The admin email is the email for the person who will receive the CSVs that this script will 
generate.  This must be within single or double quotes.

    admin_email = "admin@email.com"

The default days is what tells the script how many days back worth of time it should pull.  
Keep in mind that it will be pulling 7 days worth of time from the second you run the 
script.  Since this is a number no quotes would be used

    default_days = 7

The from address is the email that will be used as the SMTP sender.  This is who will 
deliver the email.  You will need to have the email and password as well as the host name to 
be able to use this.  This must be within single or double quotes.

    from_addr = "user@company.com"

The smtp server is the server that the emails will be sent from.  It is best if a trusted 
SMTP server is sending this and not just a self hosted as this could mean your emails end up 
in spam, that is just a suggestion though.  This must be within single or double quotes.

    smtp_server = "smtp.mail.net"

The email password is the password for the email that will be sending the CSVs.  This must 
be within single or double quotes.

    email_pass = "password"

[Back to top](https://github.com/cmtzco/zentime#zentime)


### Usage

##### Examples:

    python time.py 
    
Specify how many days back of time you need.  NOTE: The higher the number the longer the command may take.

    python time.py --days=5
or

    python time.py -n5 

[Back to top](https://github.com/cmtzco/zentime#zentime)


### Troubleshooting

##### ffi.h: No such file or directory

    c/_cffi_backend.c:15:17: fatal error: ffi.h: No such file or directory
    #include <ffi.h>
                    ^
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

This was fixed by using the apt package manager in ubuntu:

    sudo apt-get install libffi-dev

I have not tested this in other distros yet.  

##### openssl/opensslv.h: No such file or directory

    build/temp.linux-x86_64-2.7/_openssl.c:423:30: fatal error: openssl/opensslv.h: No such file or directory
    #include <openssl/opensslv.h>
                                 ^
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1


This was fixed by using the apt package manager in ubuntu:
    
    sudo apt-get install libssl-dev






