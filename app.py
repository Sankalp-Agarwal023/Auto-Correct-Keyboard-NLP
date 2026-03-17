from flask import Flask, render_template, request, jsonify
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

app = Flask(__name__)

# Load model only once when server starts
model_name = "vennify/t5-base-grammar-correction"
print("Loading T5 model... Please wait.")

tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

print("Model loaded successfully!")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/correct", methods=["POST"])
def correct():
    data = request.get_json()
    user_text = data["text"]

    input_text = "grammar: " + user_text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    outputs = model.generate(
        inputs,
        max_length=512,
        num_beams=4,
        early_stopping=True
    )

    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({
        "corrected": corrected_text
    })

if __name__ == "__main__":
    app.run(debug=False)
