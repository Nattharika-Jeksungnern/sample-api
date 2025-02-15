from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode')
def get_code():
    return "12345"

@app.route('/plus/<float:num1>/<float:num2>', methods=['GET'])
def add_numbers(num1, num2):
    result = num1 + num2
    return jsonify({'plus': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
