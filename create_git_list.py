from secrets import TOKEN
from github import Github

g = Github(TOKEN)
fstream = open('repos/giturls.txt', 'w')
for repo in g.get_user().get_repos():
    if repo.owner.login != 'fboerman':
        continue
    print(repo.full_name)
    fstream.write(repo.ssh_url+'\n')
fstream.close()