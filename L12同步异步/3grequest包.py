import requests,time
import grequests   #封装了requests和gevent包 ,基于协程技术实现并发请求
#同步请求sync
def request1():
    url_list = [
        'https://www.csdn.net/',
        'https://www.liaoxuefeng.com',
        'https://ai.taobao.com/?pid=mm_50570328_39070332_145428725',
        'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC%CD%F8&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000',
        'https://www.baidu.com/link?url=3wopgKFEFMsV3RshF4R5kjYJzZX3LTxp74hxGoIlTQ75WN0eUrLQ68ZjIHu7S8TNbWVT_86mUt0FWTIttnbuoa&ck=4364.7.64.292.298.349.704.313&shh=www.baidu.com&wd=&eqid=bc2476680012f517000000035d36a716',
        'https://www.baidu.com/link?url=IjsgJ4oJlDUCfaYhgB2SAAZRgPgVI0geM9SfIMupCEyHlDJAa5wQnIvt7iES0npk&wd=&eqid=ea7823ec0010e904000000035d36a818'
    ]
    start_time = time.time()
    for url in url_list:
        resp = requests.get(url)
    end_time = time.time()
    print(end_time-start_time)
# 同步请求缺点:代码从上到下执行,IO型运算需要等待网络传输时间,后面的请求需要等待前面请求响应结束后才开始
#解决:多进程.多线程.协程 gevent

#异步

def request2():
    url_list = [
        'https://www.csdn.net/',
        'https://www.liaoxuefeng.com',
        'https://ai.taobao.com/?pid=mm_50570328_39070332_145428725',
        'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC%CD%F8&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000',
        'https://www.baidu.com/link?url=3wopgKFEFMsV3RshF4R5kjYJzZX3LTxp74hxGoIlTQ75WN0eUrLQ68ZjIHu7S8TNbWVT_86mUt0FWTIttnbuoa&ck=4364.7.64.292.298.349.704.313&shh=www.baidu.com&wd=&eqid=bc2476680012f517000000035d36a716',
        'https://www.baidu.com/link?url=IjsgJ4oJlDUCfaYhgB2SAAZRgPgVI0geM9SfIMupCEyHlDJAa5wQnIvt7iES0npk&wd=&eqid=ea7823ec0010e904000000035d36a818'
    ]
    start_time = time.time()
    # req_list =(grequests.get(u) for u in url_list)
    req_list=[]
    for url in url_list:
        req = grequests.get(url)
        req_list.append(req)
    #批量请求,得到批量响应
    resp_list = grequests.map(req_list)
    end_time = time.time()
    print(end_time-start_time)

if __name__ == '__main__':
    request1()
    request2()