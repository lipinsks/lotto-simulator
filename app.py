from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

MAX_NUMBER = 10
BALL_COUNT = 6

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/draw')
def draw():
    # return a random draw as JSON
    numbers = random.sample(range(0, MAX_NUMBER + 1), BALL_COUNT)
    return jsonify(numbers=numbers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2137)

