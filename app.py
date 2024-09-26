from balg.boolean import Boolean

from flask import Flask, render_template, request

booleanObject = Boolean()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_data = request.form['input_data']
    result = booleanObject.expr_to_tt(input_data)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
