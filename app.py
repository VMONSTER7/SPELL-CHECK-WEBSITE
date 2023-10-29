from flask import Flask, request, render_template
from Model import SpellCheckerModule

app = Flask(__name__)

spell_checker_module = SpellCheckerModule()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell', methods=['POST', 'GET'])
def spell():
    if request.method == 'POST':
        text = request.form['text']
        corrected_text = spell_checker_module.correct_spell(text)
        return render_template('index.html', corrected_text=corrected_text)

@app.route('/files', methods=['POST', 'GET'])
def files():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            readable_file = file.read().decode('utf-8', errors='ignore')
            corrected_file = spell_checker_module.correct_spell(readable_file)
            return render_template('index.html', corrected_file=corrected_file)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
