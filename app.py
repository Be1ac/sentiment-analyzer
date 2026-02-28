from flask import Flask, render_template, request
from main import run_analysis

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        topic = request.form.get('topic')
        results = run_analysis(topic)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)