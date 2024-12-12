from flask import Blueprint, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fi")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-fi")

bp = Blueprint('translation', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():

    translation = None  # Initialize translation result

    if request.method == 'POST':
        # Extract user input from the form
        user_input = request.form['text']

        if not user_input:
            return jsonify({"error": "No input text provided."}), 400

        try:
            # Translate the input text
            inputs = tokenizer.encode(user_input, return_tensors="pt")
            outputs = model.generate(inputs)
            translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            return jsonify({"error": "An error occurred while processing your request"}), 500

    # Render the form page for GET requests
    return render_template('index.html', translation=translation)