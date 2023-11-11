import requests
import argparse
import pandas as pd
from openpyxl import Workbook

def generate_excel():
    return 0
    # return new excel

# Parse command line arguments
parser = argparse.ArgumentParser(description="Client for the task")
parser.add_argument("-k", "--keys", nargs='+', help="Additional columns to consider")
parser.add_argument("-c", "--colored", action="store_true", help="Enable row coloring")
args = parser.parse_args()

df = pd.read_csv("vehicles.csv")


url = "http://localhost:8000/upload-excel"  # Replace with your FastAPI server's URL, i put my local host
file_path = "vehicles.csv"  

files = {"file": ("vehicles.csv", open("vehicles.csv", "rb"))}
response = requests.post(url, files=files)

if response.status_code == 200:
    data = response.json()

    # Process the JSON data and generate the Excel file as per the requirements
    generate_excel(data, args.keys, args.colored)
else:
    print(f"Failed to upload the file. Status code: {response.status_code}")





