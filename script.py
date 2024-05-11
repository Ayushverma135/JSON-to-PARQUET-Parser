import json
import xml.etree.ElementTree as ET
# import xml.dom.minidom
import pandas as pd

with open("json_data.json", "r") as json_file:
    json_data = json.load(json_file)

df = pd.DataFrame(json_data)

# Define the path for the output Parquet file
parquet_file_path = 'output.parquet'

# Write the DataFrame to a Parquet file
df.to_parquet(parquet_file_path)

print("Parquet file has been created and data has been stored.")