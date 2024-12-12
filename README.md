# Translation Flask App

A Flask application that translates user input text from English to Finnish using the `Helsinki-NLP/opus-mt-en-fi` model provided by Hugging Face.

## Features

- Simple and interactive web interface
- Uses transformer-based model for translation
- Handles input from users and provides output in JSON format

## Prerequisites

- Python 3.12 or newer

## Installation

1. Clone the repository:

   - git clone https://github.com/RabindraManandhar/translation_flaskapp.git
   - cd translation_flaskapp

2. Create and activate a virtual environment
    
   - python3 -m venv venv
   - source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install the application and its dependencies
    
   - pip install .

4. Configuration Using .env

   The app supports configuration using a '.env' file. Create a '.env' file in the root directory with the following variables:

   - FLASK_RUN_HOST=0.0.0.0
   - FLASK_RUN_PORT=5000
   - FLASK_DEBUG=True 
   - SECRET_KEY=my-secret-key
   
4. Running the application
   - run-translation-app
