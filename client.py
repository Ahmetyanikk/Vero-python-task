import requests

url = "http://localhost:8000/upload-excel"  # Replace with your FastAPI server's URL, i put my local host
file_path = "vehicles.csv"  

files = {"file": open(file_path, "rb")}
response = requests.post(url, files=files)

if response.status_code == 200:
    print("File successfully uploaded to the server.")
else:
    print(f"Failed to upload the file. Status code: {response.status_code}")



