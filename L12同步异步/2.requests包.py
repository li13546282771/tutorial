import requests
# requests包是python http请求中最为知名的第三方包,封装程度较高
# py2  urllib  urllib2   都是内置包,urllib2补充了一些方法  py2脚本中这两个包同时使用
# py3 只有urllib把2版本两个包合并
# urllib3:第三方包,封装高,一般不直接使用
# requests(推荐):基于urllib3封装  非常流行
# 简单get请求
def request1():
    resp = requests.get(url='http://www.baidu.com')
    print(resp)   #<Response [200]>
    status_code = resp.status_code
    print(status_code)#状态码

    print(resp.content)#网页html字符串信息经过encode()编码后的二进制信息\xa6\xe4\二进制的十六进制表示

    print(resp.content.decode(encoding='utf-8'))   #手动解码

    print(resp.text)   #resp.content.decode()自动解码得到网页html字符串信息 注意:包有时会误判编码方式

#get请求带参数
def request2():
    # resp = requests.get(url='http://www.baidu.com/s?wd=学习')
    resp = requests.get(url='http://www.baidu.com/s',params={'wd':'学习'})#parameter参数
    #中文参数会进行base64编码'http://www.baidu.com/s?wd=%E5%AD%A6%E4%B9%A0'
    if resp.status_code == 200:
        html_text = resp.content.decode(encoding='utf-8')
        print(html_text)
    else:
        pass
def request3():
    # 自定义headers请求头
    #request包默认的请求头User-agent为"python-requests"
    headers = {
        "User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0',
        "Cookie":""
    }
    Cookie = {}
    requests.get(url='http://www.baidu.com/s',headers=headers)
    # requests.get(url='http://www.baidu.com/s',headers=headers,Cookie=Cookie)

def request4():

    params = {
        'name': '张',
    }
    response = requests.post('http://127.0.0.1:8000/login/register_check/', data=params)
    print(response.text)


def request5():
    #非重点)代理
    ip="111.231.140.109"
    port ='8888'
    proxies = {"http":f"http://{ip}:{port}"}
    resp=requests.get(url="http://www.baidu.com/s?wd=ip",proxies=proxies)
    print(resp.content.decode('utf-8'))
if __name__ == '__main__':
    request4()
    #
    # {"status": 0,
    #  "result": {"location": {"lng": 112.54661389523005, "lat": 37.90125558514076},
    #             "precise": 1, "confidence": 70,
    #             "comprehension": 100,
    #             "level": "UNKNOWN"}}