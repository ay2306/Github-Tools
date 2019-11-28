import requests
import json
import sys
sys.stdout = open('result.md','w')
page = 1
per_page = 100
while True:
    try:
        user_list = requests.get('https://api.github.com/repos/ipfs/js-ipfs-http-client/contributors?per_page='+str(per_page)+'&page='+str(page))
        data = user_list.json()
        # print(len(data))
        # print(data)
        if(len(data) == 0):
            break
        for user in data:
            print(f"[] @[{user['login']}](https://github.com/{user['login']})({user['contributions']})")
        page+=1
    except:
        break