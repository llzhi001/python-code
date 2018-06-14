#1.send a get request
import requests
response = requests.get("http://httpbin.org/ip")
print("content:",response.text)

#2.add parameters
parameter = {'url':'https://www.bing.com'}
response = requests.get("http://httpbin.org/redirect-to", params=parameter)
#print("content:", response.text)

#3.status code
print("status code:", response.status_code)

#4.headers
response = requests.get("http://httpbin.org/headers")
for header,value in response.headers.items():
    print(header,"::", value)
print("status code:", response.status_code)

#5.set a header to trick the server
response = requests.get("http://httpbin.org/headers")
print("content:", response.text)
header = {"user-agent":"Android phone"}
response = requests.get("http://httpbin.org/headers", headers = header)
print("content:", response.text)

#6.post method
response = requests.post("http://httpbin.org/post", data = {"username":'henry',"password":12345, "phone number":123456789})
print("content:", response.text)
