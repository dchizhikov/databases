import git.config as config
import requests

def getModuleGitHub(file_git='git_commands.py', file_local='git_com.py'):
  url = "https://raw.githubusercontent.com/"+config.user_name+"/"+config.repo_name_git+"/main/"+file_git
  response = requests.get(url)
  
  with open(f'{config.repo_up}/{file_local}', 'w') as f:
    f.write(response.text)

#getModuleGitHub('git_commands.py', 'git_com.py')
