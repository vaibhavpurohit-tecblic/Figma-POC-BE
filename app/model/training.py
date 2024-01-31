# training.py

import os
import json
from bs4 import BeautifulSoup
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

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

    soup = BeautifulSoup(html_content, 'html.parser')
    text_tokens = soup.stripped_strings

    return ' '.join(text_tokens)

# Directory paths for JSON and HTML files
json_files_dir = "dataset/login/train/json"
html_files_dir = "dataset/login/train/html"

# we are storing texts and labels here
texts = []
labels = []

# for JSON files
for json_file_name in os.listdir(json_files_dir):
    if json_file_name.endswith('.json'):
        json_file_path = os.path.join(json_files_dir, json_file_name)
        json_tokens = tokenize_json(json_file_path)
        texts.append(json_tokens)
        labels.append(1)  # Set the label based on your task

# Processing HTML files here
for html_file_name in os.listdir(html_files_dir):
    if html_file_name.endswith('.html'):
        html_file_path = os.path.join(html_files_dir, html_file_name)
        html_tokens = tokenize_html(html_file_path)
        texts.append(html_tokens)
        labels.append(0)  # we can set the label based on our task

# we can tokenize the text data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

# here, we are Converting text to sequences
sequences = tokenizer.texts_to_sequences(texts)

# Pad sequences to a fixed length
max_len = 100
# Set your desired maximum sequence length
padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post')

# Convert labels to numpy array
labels = tf.keras.utils.to_categorical(labels, num_classes=2)  # Assuming binary classification

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42)

# Build a simple neural network model (modify as needed)
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=50, input_length=max_len),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')  # Adjust based on the number of classes
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=25, batch_size=64, validation_data=(X_test, y_test))

model.save('models/login_model.h5')
