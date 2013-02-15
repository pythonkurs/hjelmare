import datetime
import getpass
import requests
import sys

from dateutil import parser
from pandas import DataFrame
from pandas import Series

# Function to get the user's GitHub username
def get_username():
    username = raw_input("Enter your GitHub username: ")
    return username

# Function to get the user's GitHub password
def get_password():
    password = getpass.getpass("Enter your GitHub password: ")
    return password

# Function for GET with exception catching
def get_request(uri, user, password):
    try:
        request = requests.get(uri, auth=(user, password))
    except requests.ConnectionError:
        print("Got connection error. Check network.")
        sys.exit()
    if not request.status_code == 200:
        if not request.status_code == 409:
            print("Webserver error, status code: "+str(request.status_code)+". Try again later.")
            sys.exit()
        else:
            pass
    return request


# Function should return a DataFrame
def github_repo():

    username = get_username()
    password = get_password()

    users = get_request("https://api.github.com/orgs/pythonkurs/members", username, password)
    repos = get_request("https://api.github.com/orgs/pythonkurs/repos", username, password)
    users_data = users.json()
    repos_data = repos.json()

    # Print the number of users in the org.  
    print("There are "+str(len(users_data))+" users in the organization.")

    # Print the number of repos in the org.  
    print("There are "+str(len(repos_data))+" repos in the organization.")

    d = {}

    for repo in repos_data:
        # Print all repos in the org
        print(repo['full_name'])
        commits_data = get_request("https://api.github.com/repos/"+repo['full_name']+"/commits", username, password).json()
        date_list = []
        message_list = []
        for commit in commits_data:
            try:
                message = str(commit['commit']['message'])
                date = commit['commit']['committer']['date']
                date_time = parser.parse(date)
                date_time = date_time.replace(tzinfo=None)
                date_list.append(date_time)
                message_list.append(message)
                # Print all messages per date made sorted per repo in the org
                #print(date+" : "+message)
            except TypeError:
                print(commits_data['message']+" @ "+repo['full_name'])
        # import pdb; pdb.set_trace()
        s = Series(message_list, index=date_list, name=repo['full_name'])
        d[repo['full_name']] = s

    df = DataFrame(d)

    return df

# Function which takes a DataFrame as argument and prints the weekday and hour of a day when most commits have been made.  
def social_log():
    df = github_repo()
    #date_time.isoweekday()
    #date_time.hour
    print(df)
