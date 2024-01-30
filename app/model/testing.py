import os
import json
import tensorflow as tf
from zipfile import ZipFile
from bs4 import BeautifulSoup
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from app.model.config import TRAIN_HTML_DIR, MODEL_PATH

# unzipping 
def unzip_data():
    folder_name = 'app/model/dataset'
    extraction_path = 'app/model'

    # Get the current directory
    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, folder_name)

    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        print(f"The folder '{folder_name}' exists in the current directory.")
    else:
        print(f"The folder '{folder_path}' does not exist ,we'll create it.")
        # Open the zip file
        with ZipFile(f'{folder_path}.zip', 'r') as zip_ref:
            print('Extracting dataset...')

            # Extract all the files
            zip_ref.extractall(extraction_path)
            print('Dataset created at location: ',extraction_path )

# Function to tokenize input JSON file
def tokenize_input_json(input_json_file_path):
    with open(input_json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    tokens = [f'{key} {str(value)}' for key, value in json_data.items()]
    return ' '.join(tokens)

# Function to predict HTML content for a given JSON input
def predict_html_content_for_json(input_json_tokens, tokenizer, max_len, loaded_model, html_files_dir):
    # Tokenize text data
    input_sequences = tokenizer.texts_to_sequences([input_json_tokens])

    # Pad sequences to a fixed length
    input_padded_sequences = pad_sequences(input_sequences, maxlen=max_len, padding='post')

    # Make predictions using the loaded model
    prediction = loaded_model.predict(input_padded_sequences)

    # Assuming binary
    # Return HTML content classification, check the predicted label
    predicted_label = 1 if prediction[0][1] > 0.5 else 0

    # Determine the corresponding HTML file based on the predicted label
    html_files = os.listdir(html_files_dir)
    predicted_html_file_path = os.path.join(html_files_dir, html_files[predicted_label])

    # Read the content of the predicted HTML file
    with open(predicted_html_file_path, 'r', encoding='utf-8') as html_file:
        predicted_html_content = html_file.read()

    return predicted_html_content

# Function to generate HTML file for a given JSON input
def generate_html_for_json(input_json_file_path, tokenizer, max_len, loaded_model, html_files_dir, output_html_path):
    # extracting dataset from zip file
    unzip_data()
    
    # Tokenize input JSON
    input_json_tokens = tokenize_input_json(input_json_file_path)

    # Predict HTML content for the given JSON input
    predicted_html_content = predict_html_content_for_json(input_json_tokens, tokenizer, max_len, loaded_model, html_files_dir)

    # Save the predicted HTML content to a new HTML file
    with open(output_html_path, 'w', encoding='utf-8') as output_html_file:
        output_html_file.write(predicted_html_content)

    return predicted_html_content

def generate_html(json_file_name):
    # Set paths
    json_file_path = f'app/output_json/{json_file_name}'

    json_name_without_ext, _ = os.path.splitext(json_file_name)

    output_html_path = f'app/model/model_output/{json_name_without_ext}.html'

    # Load trained model
    loaded_model = tf.keras.models.load_model(MODEL_PATH)

    # Load tokenizer
    tokenizer = Tokenizer()

    # Generate HTML file for a given JSON input
    html_content = generate_html_for_json(json_file_path, tokenizer, max_len=100, loaded_model=loaded_model, html_files_dir=TRAIN_HTML_DIR, output_html_path=output_html_path)
    print(f'The HTML file has been generated: {output_html_path}')

    return html_content
