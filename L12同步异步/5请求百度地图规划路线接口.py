import requests,json


#计算ip接口
base_ip ='http://api.map.baidu.com/geocoding/v3'
params ={
    'address':'山西省太原市林业职业技术学院',
    "output":'json',   #json或xml
    "ak":'nazZGPjoTnQQLm7uW8VTXr6muI5n5hIr'
}
resp = requests.get(url=base_ip,params=params)
status_code = resp.status_code

resp_json =resp.text
resp_json =json.loads(resp_json)
lng = resp_json['result']['location']['lng']   #经
lat = resp_json['result']['location']['lat']   #纬


# 起点经纬度
p ={
    'address':'山西省太原市城市职业技术学院',
    "output":'json',   #json或xml
    "ak":'nazZGPjoTnQQLm7uW8VTXr6muI5n5hIr'
}
response = requests.get(url=base_ip,params=p)
resp_json1 =response.text
resp_json1 =json.loads(resp_json1)
lng1 = resp_json1['result']['location']['lng']   #经
lat1 = resp_json1['result']['location']['lat']   #纬


#
base_url = 'http://api.map.baidu.com/direction/v2/transit'
p2 ={

    'origin':f'{lat1},{lng1}',
'destination':f'{lat},{lng}',
    'coord_type':'bd09ll',
    "output":'json',
    # 'trans_type_intercity':1,
    # "vehicle_info":1,
    "ak":'nazZGPjoTnQQLm7uW8VTXr6muI5n5hIr',

}
resp2 = requests.get(url=base_url,params=p2)
status_code2 = resp2.status_code

resp_json2 =resp2.text
print(resp_json2)

