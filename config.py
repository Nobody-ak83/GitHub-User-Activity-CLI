from github import Github
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN= os.getenv("GITHUB_TOKEN")

if not TOKEN:
    raise ValueError("NO TOKEN FOUND!")




def getGitUserActivity(username):
    
    
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, headers=headers)

    if response.status_code==200:
        events=response.json()
        
    
        for event in events[:30]:
            event_type=event.get('type')
            repo_name=event.get('repo', {}).get('name')
            created_at=event.get('created_at')
            
            if event_type=='PushEvent':
                commits=event.get('payload', {}).get('commits',[])
                print(f'[{created_at}] Push at repo {repo_name}')
                for commit in commits:
                    print(f' - Commit: {commit.get("message")}')
                    
            elif event_type == "WatchEvent":
                action = event.get("payload", {}).get("action")
                if action == "started":
                    print(f"[{created_at}] Stared repo {repo_name}")
            
            elif event_type == "CreateEvent":
                ref_type = event.get("payload", {}).get("ref_type")  
                ref = event.get("payload", {}).get("ref")  
                print(f"[{created_at}]  Created {ref_type} '{ref}' in {repo_name}")
                
        
            elif event_type == "PullRequestEvent":
                action = event.get("payload", {}).get("action")  
                pr_title = event.get("payload", {}).get("pull_request", {}).get("title")
                print(f"[{created_at}]  {action.capitalize()} pull-request '{pr_title}' in {repo_name}")
                
            else:
                print(f"[{created_at}] Other activity: {event_type} in {repo_name}")
            
    else:
        print(f"Can't get data. Code: {response.status_code}")