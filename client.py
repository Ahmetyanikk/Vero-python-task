import requests

url = "http://localhost:8000/upload-excel"  # Replace with your FastAPI server's URL, i put my local host
file_path = "vehicles.csv"  

files = {"file": open(file_path, "rb")}
response = requests.post(url, files=files)

if response.status_code == 200:
    print("File successfully uploaded to the server.")
else:
    print(f"Failed to upload the file. Status code: {response.status_code}")

url = "https://api.baubuddy.de/index.php/login"
payload = {
    "username": "365",
    "password": "1"
}
headers = {
    "Authorization": "Basic QVBJX0V4cGxvcmVyOjEyMzQ1NmlzQUxhbWVQYXNz",
    "Content-Type": "application/json"
}
response = requests.request("POST", url, json=payload, headers=headers)
temp=response.text.split('"')
print(temp)


