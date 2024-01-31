import os
import json
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from bs4 import BeautifulSoup
from app.model.config import MODEL_PATH, INPUT_JSON_FILE_PATH, OUTPUT_HTML_PATH, HTML_FILES_DIR

max_len = 100

# Function to tokenize JSON file
def tokenize_json(json_file_path):
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    tokens = []
    for key, value in json_data.items():
        tokens.extend([key, str(value)])  # Add key and value as tokens

    return ' '.join(tokens)

# Function to tokenize HTML file
def tokenize_html(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    # Using BeautifulSoup to extract text content
    soup = BeautifulSoup(html_content, 'html.parser')
    text_tokens = soup.stripped_strings

    return ' '.join(text_tokens)

# Function to predict HTML content for a given JSON input
def predict_html_content_for_json(input_json_tokens, tokenizer, max_len, loaded_model, html_files_dir):
    # Tokenize text data
    input_sequences = tokenizer.texts_to_sequences([input_json_tokens])

    # Pad sequences to a fixed length
    input_padded_sequences = pad_sequences(input_sequences, maxlen=max_len, padding='post')

    # Make predictions using the loaded model
    prediction = loaded_model.predict(input_padded_sequences)

    # Assuming binary classification, check the predicted label
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
    # Tokenize input JSON
    input_json_tokens = tokenize_json(input_json_file_path)

    # Predict HTML content for the given JSON input
    predicted_html_content = predict_html_content_for_json(input_json_tokens, tokenizer, max_len, loaded_model, html_files_dir)

    # Save the predicted HTML content to a new HTML file
    with open(output_html_path, 'w', encoding='utf-8') as output_html_file:
        output_html_file.write(predicted_html_content)

    return predicted_html_content

def generate_html(json_file_name):
    # Directory paths for HTML files
    # html_files_dir = 'dataset/login/train/html'
    html_files_dir = HTML_FILES_DIR

    # Load the model back for predictions
    loaded_model = tf.keras.models.load_model(MODEL_PATH)

    # Tokenizer for text data
    tokenizer = Tokenizer()

    # Example usage for generating HTML file for a given JSON input
    # input_json_file_path = 'dataset/login/test/login1.json'
    input_json_file_path = INPUT_JSON_FILE_PATH
    # input_json_file_path = 'new.json'
    # output_html_path = 'output/login/login_output.html'
    output_html_path = OUTPUT_HTML_PATH

    html_content = generate_html_for_json(input_json_file_path, tokenizer, max_len, loaded_model, html_files_dir, output_html_path)
    print(f"The HTML file has been generated: {output_html_path}")
    return html_content
