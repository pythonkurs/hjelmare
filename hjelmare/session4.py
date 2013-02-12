import requests, datetime
from dateutil import parser

#Function should return a DataFrame
#pass the path to the credentials as an argument when calling the github_repo function
def github_repo(secret):
    with open(secret) as secret:
        password = secret.read().strip()

    try:
        users = requests.get("https://api.github.com/orgs/pythonkurs/members", auth=("MartinHjelmare", password))

    except requests.ConnectionError:
        print("Got connection error. Check network.")
        sys.exit()
    if not users.status_code == 200:
        print("Webserver error, status code: "+str(users.status_code)+". Try again later.")
        sys.exit()

    users_data = users.json()
    number_users=len(users_data)
    print("There are "+str(number_users)+" users in the organization.")
    


#A function which takes a DataFrame as argument and returns the weekday and hour of a day
