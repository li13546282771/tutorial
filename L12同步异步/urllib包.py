import urllib.request
response = urllib.request.urlopen('http://www.baidu.com/')
print(response)
print(response.code)#状态码
html_content = response.read()
print(html_content)
print(html_content.decode(encoding ='utf-8'))
