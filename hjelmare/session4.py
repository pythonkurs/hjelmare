import datetime
import getpass
import requests

from dateutil import parser
from pandas import DataFrame
from pandas import Series

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

    password = get_password()

    users = get_request("https://api.github.com/orgs/pythonkurs/members", "MartinHjelmare", password)
    repos = get_request("https://api.github.com/orgs/pythonkurs/repos", "MartinHjelmare", password)
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
        commits_data = get_request("https://api.github.com/repos/"+repo['full_name']+"/commits", "MartinHjelmare", password).json()
        date_list = []
        message_list = []
        for commit in commits_data:
            try:
                date = commit['commit']['committer']['date']
                message = commit['commit']['message']
                date_list.append(date)
                message_list.append(message)
                # Print all messages per date made sorted per repo in the org
                #print(date+" : "+message)
            except TypeError:
                print(commits_data['message'])
        # import pdb; pdb.set_trace()
        s = Series(message_list, index=date_list, name=repo['full_name'])
        d[repo['full_name']] = s

    df = DataFrame(d)

    return df


#s = Series(["A commit message"] * 5, index=date_list, name="A repo")

#d = {'one' : Series([1., 2., 3.], index=['a', 'b', 'c']), \
#     'two' : Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

#df = DataFrame(d)
#df






#List repositories for the specified org.
#working
#GET /orgs/:org/repos
#https://api.github.com/orgs/pythonkurs/repos
#org_repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=("MartinHjelmare", password))

#List commits for the specified repo.
#working
#/repos/:owner/:repo/commits
#https://api.github.com/repos/pythonkurs/hjelmare/commits
#org_commits = requests.get("https://api.github.com/repos/pythonkurs/hjelmare/commits", auth=("MartinHjelmare", password))

#working
#/orgs/:org/events
#https://api.github.com/orgs/pythonkurs/events
#public_events = requests.get("https://api.github.com/orgs/pythonkurs/events", auth=("MartinHjelmare", password))

#working
#/users/:user/events/orgs/:org
#https://api.github.com/users/MartinHjelmare/events/orgs/pythonkurs
#events = requests.get("https://api.github.com/users/MartinHjelmare/events/orgs/pythonkurs", auth=("MartinHjelmare", password))




# Function which takes a DataFrame as argument and returns the weekday and hour of a day when most commits have been made.  
def social_log():
    df = github_repo()
    print(df)
