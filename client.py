import requests
import argparse
import pandas as pd
from openpyxl import Workbook


# Parse command line arguments
parser = argparse.ArgumentParser(description="Client for the task")
parser.add_argument("-k", "--keys", type=str,default='',action='store',nargs='+', help="Additional columns to consider")
parser.add_argument("-c", "--colored", action="store_false", help="Enable row coloring")
args = parser.parse_args()
data = {
    'keys': args.keys,
    'colored': args.colored
}
print(data)


url = "http://localhost:8000/upload-excel"  # Replace with your FastAPI server's URL, i put my local host
file_path = r"C:\Users\Ahmet\PycharmProjects\untitled8\vehicles.csv"

files = {"file": ("vehicles.csv", open("vehicles.csv", "rb"))}
response = requests.post(url,files=files)
if response.status_code == 200:
    print(response.text)
    # Process the JSON data and generate the Excel file as per the requirements
else:
    print(f"Failed to upload the file. Status code: {response.status_code}")




