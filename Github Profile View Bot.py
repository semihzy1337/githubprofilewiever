import requests

def send_requests(url, count):
    for i in range(count):
        try:
            response = requests.get(url)
            print(f"istek basarili {i+1}: Resp Kodu = {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"istek basarisiz {i+1}: Hata kodu: {e}")

url = 'https://camo.githubusercontent.com/f5d3432c3d9c7fec2b26e2595800990abe48f429a6da2216324f537a393bf67d/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d73656d69687a7931333337'
count = 1000000
send_requests(url, count)
    