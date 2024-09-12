import requests #библиотека для отправки запросов
data = { "login": "TelegramBot", "password": "1234" }
headers = {  "Authorization": "Bearer <token>" }
files = { "file": open(<path>, "rb" ) }
response = requests.post("http://localhost:8000/api/auth/login", json=data, headers=headers, files=files)
print(response.status_code)
print(response.json())
