#Get pull request information on a repository using python
#the repository we selected is kubernetes
#Before writing the first piece of code, first install requests in your folder (pip install requests)

#now import requests

import requests

requests.get("api.github.com/repos/kubernetes/kubernetes/pulls")




