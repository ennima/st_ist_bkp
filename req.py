import requests,json
url = 'http://127.0.0.1:3000/store_clip'
data = '{"name":"Clip1",}'
data = '{}'

dic_test = {"name":"Clip1"
,"created_date":"19/12/2017 08:54:31 p.m."
,"modified_date":"19/12/2017 08:54:31 p.m."
,"duration":""
,"path":""
,"has_pxy":0
,"archived_date":"2017-12-27 00:00:00"
,"archived_user":"developer"
,"original_path":""
,"format":1
,"origin":1
,"storage":4
}
# print(json.dumps(dic_test))
data = json.dumps(dic_test)
response = requests.post(url, data=data,headers={"Content-Type": "application/json"})
print(response.json())