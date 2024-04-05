import requests

url = "http:/api/method/my_module.MyClass.my_method"
data = {
    "param1": "value1",
    "param2": "value2"
}

response = requests.post(url, json=data)
print(response.json())
