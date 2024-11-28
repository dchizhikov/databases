import os

current_file_path = __file__
directory_path = os.path.dirname(current_file_path)
folder_name = os.path.basename(directory_path)
parent_directory_path = os.path.dirname(directory_path)

user_name = "dchizhikov"
repo_name_git = "git"

repo_up = parent_directory_path
repo_name = "git" #['git', 'UML', 'databases', 'Telegram', 'tg_bot']
myRepo = repo_up + '/'+repo_name

repo_url = "https://github.com/"+user_name+"/"+repo_name

public_token = os.environ["public_token"]
#private_token = os.environ["PAT"]
_token = public_token #[public_token, private_token]

branch = "origin_479F" #"origin_tg_479F" "origin_479F"
remote_branch = "main"