import requests
import sys 
import datetime 

def fetch_github_activity(user_name): 
    """Fetches user activity in Github:
    Repository creation/deletion, issue creation, pull requests, starred repositories, forked repositories."""
    
    url = f"https://api.github.com/users/{user_name}/events"
    response = requests.get(url)

    if response.status_code == 404:
        return f"User '{user_name}' not found."
    elif response.status_code != 200:
        return f"Error fetching data: {response.status_code}"

    events = response.json()

    if not events:
        return f"User {user_name} has no recent activity."

    commit_count = {}
    event_log = f"Activity for user {user_name} - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}:\n"

    for event in events:
        if event['type'] == 'PushEvent':
            repo_name = event['repo']['name']
            if repo_name in commit_count:
                commit_count[repo_name].append(1)
            else:
                commit_count[repo_name] = [1]
        elif event['type'] == "IssueCommentEvent":
            event_log += f"- Added comment on issue #{event['payload']['issue']['number']}.\n"
        elif event['type'] == "CreateEvent":
            event_log += f"- Created repository: {event['repo']['name']}.\n"
        elif event['type'] == "WatchEvent": 
            event_log += f"- Added star to repository: {event['repo']['name']}.\n"
        elif event['type'] == "PullRequestEvent":
            event_log += f"- Created Pull Request for repository: {event['repo']['name']}.\n"
        elif event['type'] == "DeleteEvent":
            event_log += f"- Deleted repository: {event['repo']['name']}.\n"
        elif event['type'] == "ForkEvent":
            event_log += f"- Forked repository: {event['repo']['name']}.\n"

    for repo, pushes in commit_count.items():
        event_log += f"- Pushed {len(pushes)} times in repository: {repo}.\n"
    
    return event_log

if __name__ == '__main__':
    if len(sys.argv) > 1: 
        print(fetch_github_activity(sys.argv[1]))
    else: 
        print("Username not valid! Please provide a valid username. ")