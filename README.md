# Zentime

### Easily export time from Zendesk to import to JIRA

### Installation

Commands to run to install zentime requirements

    sudo ./install.sh

### Configuration

In the config.py file you will see all the variables that need to be set in order for this 
to work with your Zendesk account.  Be sure that you have Admin access to your Zendesk 
instance if not you will not be able to proceed with getting a token on your own.  

### Usage

#### Examples:

    python time.py 
    
Specify how many days back of time you need.  NOTE: The higher the number the longer the command may take.

    python time.py --days=5
or

    python time.py -n5 

