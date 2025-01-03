import csv
import json
from typing import List, Union, Dict


def read_csv(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
        return data

def print_csv_content(data: List[Dict[str, str]]):
   
    for row in data:
        print("; ".join([f"{key} → {value}" for key, value in row.items()]))

def calculate_min(data: List[Dict[str, str]], column: str) -> Union[float, int, None]:
    
    try:
        return min(float(row[column]) for row in data if row[column])
    except ValueError:
        return None

def calculate_max(data: List[Dict[str, str]], column: str) -> Union[float, int, None]:
   
    try:
        return max(float(row[column]) for row in data if row[column])
    except ValueError:
        return None

def calculate_sum(data: List[Dict[str, str]], column: str) -> Union[float, int]:
    
    return sum(float(row[column]) for row in data if row[column])

def calculate_avg(data: List[Dict[str, str]], column: str) -> Union[float, None]:
   
    values = [float(row[column]) for row in data if row[column]]
    return sum(values) / len(values) if values else None

# 2 пункт
def read_json(file_path: str) -> Dict:
    
    with open(file_path, 'r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile)

def filter_users_by_version(data: List[Dict], version: str) -> List[Dict]:
    
    return [user for user in data if user.get('version') == version]

def write_json(file_path: str, data: List[Dict]):
    
    with open(file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    
    csv_data = read_csv("12.csv")
    print_csv_content(csv_data)

    column_name = "your_column_name"  
    print("Min:", calculate_min(csv_data, column_name))
    print("Max:", calculate_max(csv_data, column_name))
    print("Sum:", calculate_sum(csv_data, column_name))
    print("Avg:", calculate_avg(csv_data, column_name))

    
    json_data = read_json("lab.json")
    filtered_users = filter_users_by_version(json_data, "1.0")  
    write_json("out.json", filtered_users)