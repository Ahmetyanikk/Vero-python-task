import requests
import argparse
import pandas as pd
from openpyxl import Workbook



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


else:
    print(f"Failed to upload the file. Status code: {response.status_code}")





