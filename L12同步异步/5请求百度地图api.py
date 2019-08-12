# 后端接口只需定义好规则,写好逻辑,返回数据..有些公司开发好特定功能的接口拿来售卖
# 其他公司或产品可以直接调用别人写好的功能,提高开发的效率,例如滴滴就是用了高德地图api
# api版本,有些api url中看到v2表示服务端api的第2个大版本,因为服务器接口逻辑会变化,但又不能影响老用户,多版本共存,看文档注意
# sn  sing number 签名吗  一般是所有参数按key名排序,得到的字符串hash加密得到加密后字符串,服务器接收到请求后会再计算一遍sn,如果跟客户端发送的sn一致,不一致就认为参数被攻击者修改,丢弃请求
import requests

# 百度地图api搜索附近功能 http://lbsyun.baidu.com/apiconsole/key
# #access key  接入权限的秘钥,标识用户;调用计次收费  其他平台的api可能会在headers中cookie携带
base_url = 'http://api.map.baidu.com/place/v2/search'
params = {
    "query":"火锅",
    "region":'176',
    "output":'json',   #json或xml
    "ak":'nazZGPjoTnQQLm7uW8VTXr6muI5n5hIr'
}
resp = requests.get(url=base_url,params=params,timeout=5)
status_code = resp.status_code
print(status_code)
resp_json =resp.text
print(resp_json)