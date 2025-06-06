from flask import Flask, request, jsonify
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = Flask(__name__)

model = T5ForConditionalGeneration.from_pretrained("movie-summary-model")
tokenizer = T5Tokenizer.from_pretrained("movie-summary-model")

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    plot = data.get("plot")
    inputs = tokenizer("summarize: " + plot, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=100, min_length=30, length_penalty=2.0, num_beams=4)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
