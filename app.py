from flask import Flask, render_template, request
from main import run_analysis

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    summary = None
    if request.method == 'POST':
        topic = request.form.get('topic')
        results, summary = run_analysis(topic) # Get both values
    return render_template('index.html', results=results, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)