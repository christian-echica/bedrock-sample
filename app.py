from flask import Flask, request, render_template
from inference import get_model_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    prompt = request.form['prompt']
    model_response = get_model_response(prompt)
    return render_template('result.html', result=model_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

