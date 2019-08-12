import requests,base64
url ='http://192.168.119.119:5000/award_img/'
resp = requests.post(url=url)
bianma = resp.content.decode(encoding='utf-8')
content =base64.b64decode(bianma)

with open('红包.png','wb')as file:
    file.write(content)
    