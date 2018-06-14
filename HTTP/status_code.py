import requests
#1.success
url = "http://httpbin.org/html"
response = requests.get(url)
print("response code:", response.status_code)

#2.not found
url = "http://httpbin.org/htmlXXXX"
response = requests.get(url)
print("response code:", response.status_code)

#.redirection
url = "http://httpbin.org/redirect-to"
parameters = {"url":"https://www.bing.com"}
response = requests.get(url,params = parameters)
print(response.text)
print("response code:", response.status_code)
print("response url:", response.url)
for resp in response.history:
    print("response code:", resp.status_code)
    print("response url:", resp.url)
