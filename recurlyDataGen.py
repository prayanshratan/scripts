import requests
import time

count = 0
for i in range(730000, 9300001):
    count += 1
    url = "https://v3.recurly.com/accounts"
    payload = {
        "code": f"testing_2-{i}",
        "username": f"test new account {i}",
        "email": f"user{i}@example.com"
    }
    headers = {
        "Accept": "application/vnd.recurly.latest",
        "Authorization": "Basic MjRiNTFlMjk5YTk4NGQ3M2JhZTFjMjM3MWZmN2I2ZDE6",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"send request - {count}")
    print(response.json())
    time.sleep(2)
