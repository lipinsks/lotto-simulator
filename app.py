from flask import Flask, jsonify, render_template, request, Response
import random, json

app = Flask(__name__)
MAX_NUMBER = 49
BALL_COUNT = 6
COST_PER_DRAW = 12

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/simulate')
def simulate():
    picks = request.args.getlist('picks', type=int)

    def generate():
        counter = 0
        while True:
            counter += 1
            draw = random.sample(range(1, MAX_NUMBER + 1), BALL_COUNT)

            if counter % 100000 == 0:
                cost = counter * COST_PER_DRAW
                yield f"data: {json.dumps({'counter': counter, 'drawPreview': draw, 'cost': cost})}\n\n"

            if set(draw) == set(picks):
                cost = counter * COST_PER_DRAW
                yield f"data: {json.dumps({'counter': counter, 'draw': draw, 'cost': cost})}\n\n"
                break

    return Response(generate(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2137)

