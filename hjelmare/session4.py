import requests, datetime
from dateutil import parser
from pandas import DataFrame


#pass the path to the credentials as an argument when calling the github_repo function

#Function for GET with exception catching
def get_request(uri, user, path_to_secret):
    with open(path_to_secret) as secret:
        password = secret.read().strip()
    try:
        request = requests.get(uri, auth=(user, password))
    except requests.ConnectionError:
        print("Got connection error. Check network.")
        sys.exit()
    if not request.status_code == 200:
        print("Webserver error, status code: "+str(request.status_code)+". Try again later.")
        sys.exit()
    return request


#Function should return a DataFrame
def github_repo(secret):

    users = get_request("https://api.github.com/orgs/pythonkurs/members", "MartinHjelmare", secret)
    repos = get_request("https://api.github.com/orgs/pythonkurs/repos", "MartinHjelmare", secret)

    users_data = users.json()

    #Print the number of users in the org
    print("There are "+str(len(users_data))+" users in the organization.")
    
    repos_data = repos.json()

    #Print the number of repos in the org
    print("There are "+str(len(repos_data))+" repos in the organization.")

    all_repos_commits = [len(repos_data)]
    repo_list = [len(repos_data)]
    
    i = 0
    for repo in repos_data:
        repo_list[i] = repo['full_name']
        #Print all repos in the org
        print(repo_list[i])
        all_repos_commits[i] = get_request("https://api.github.com/repos/"+repo['full_name']+"/commits", "MartinHjelmare", secret)
        commits_data = all_repos_commits[i].json()
        for commit in commits_data:
            date = commit['commit']['committer']['date']
            message = commit['commit']['message']
            #Print all messages per date made sorted per repo in the org
            print(date+" : "+message)
        i++

s = Series(["A commit message"] * 5, index=date_list, name="A repo")

d = {'one' : Series([1., 2., 3.], index=['a', 'b', 'c']), \
     'two' : Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = DataFrame(d)
df

#return DataFrame




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




#A function which takes a DataFrame as argument and returns the weekday and hour of a day
