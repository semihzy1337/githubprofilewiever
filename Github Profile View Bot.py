import requests

def send_requests(url, count):
    for i in range(count):
        try:
            response = requests.get(url)
            print(f"istek basarili {i+1}: Resp Kodu = {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"istek basarisiz {i+1}: Hata kodu: {e}")

url = ''
count = 
send_requests(url, count)
    
