import json
import os

import requests
from config import Config
from urllib.parse import urlparse, parse_qs

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(ROOT_DIR, 'output_json')
# Now, you can use OUTPUT_DIR to point to the desired directory for your files


# def generate_figma_url(base_url, node_id=None, depth=None):
def generate_figma_url(base_url, node_id=None):
    node_url = f"ids={node_id}"
    # depth_url = f"depth={depth}"

    return f"{base_url}?{node_url}"
    # return f"{base_url}?{node_url}&{depth_url}"

def extract_figma_info(url):
    parsed_url = urlparse(url)

    # Extract the file key
    file_key = None
    path_components = parsed_url.path.split('/')
    
    if 'file' in path_components:
        file_key = path_components[path_components.index('file') + 1]
        print(file_key)

    query_params = parse_qs(parsed_url.query)
    node_id = query_params.get('node-id', [''])[0]

    return file_key, node_id

def get_nodes(url):
    file_key, nodes = extract_figma_info(url)
    print('file key : ', file_key)
    print('nodes : ', nodes)

    base_url = f"https://api.figma.com/v1/files/{file_key}"

    # figma_url = generate_figma_url(base_url, nodes, depth)
    figma_url = generate_figma_url(base_url, nodes)

    headers = {
        "X-Figma-Token": Config.FIGMA_TOKEN
    }
    response = requests.get(figma_url, headers=headers)
    print('Response Received...')

    if response.status_code == 200:
        data = response.json()
        childrens = data['document']['children'][0]['children']
        data_nodes = []
        
        for children in childrens:
            is_screen = check_if_valid_screen(children.get('id'))

            if is_screen:
                data_nodes.append({
                    'node_id': children.get('id'),
                    'label': children.get('name')
                })

        return data_nodes
    else:
        print(f"Failed to fetch data: {response.status_code}")

def check_if_valid_screen(node_id):
    directory = "app/output"
    is_screen = False          
    
    for folder in os.listdir(directory):
        f = os.path.join(directory, folder)
        
        if os.path.isdir(f):
            if node_id in f:
                return True

    return is_screen  

def generate_json(url):
    # nodes = "2608%3A62"
    # nodes = '801%3A2702'
    # depth = "2"
    file_key, nodes = extract_figma_info(url)
    print('file key : ', file_key)
    print('nodes : ', nodes)

    base_url = f"https://api.figma.com/v1/files/{file_key}"

    # figma_url = generate_figma_url(base_url, nodes, depth)
    figma_url = generate_figma_url(base_url, nodes)

    headers = {
        "X-Figma-Token": Config.FIGMA_TOKEN
    }
    response = requests.get(figma_url, headers=headers)
    print('Response Received...')

    if response.status_code == 200:
        data = response.json()

        # Constructing the file path in the output_json directory
        json_name = f'Generated_Figma_json_{nodes}.json'
        file_path = os.path.join(OUTPUT_DIR,json_name )

        # Writing the JSON data to a file in a readable format
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            print('Json generated: ', file_path)

        # Reading and returning json 
        with open(file_path, 'r') as f:
            formatted_json = json.load(f)

        return json_name, formatted_json

    else:
        print(f"Failed to fetch data: {response.status_code}")

# # Function to print JSON data in a readable format
# def print_readable_json(data, indent=0):
#     # Determine the indentation
#     tab = '    ' * indent
#
#     # Check if the data is a dictionary
#     if isinstance(data, dict):
#         for key, value in data.items():
#             print(f"{tab}{key}:")
#             print_readable_json(value, indent + 1)
#
#     # Check if the data is a list
#     elif isinstance(data, list):
#         for item in data:
#             print_readable_json(item, indent + 1)
#
#     # Base case: data is neither a dict nor a list
#     else:
#         print(f"{tab}{data}")
#
#
# # Load the JSON file
# with open('figma_output.json', 'r', encoding='utf-8') as file:
#     json_data = json.load(file)
#
# # Print the JSON data in a readable format
# print_readable_json(json_data)
