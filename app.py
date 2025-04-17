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
    # read picks from query string
    picks = request.args.getlist('picks', type=int)

    def generate():
        counter = 0
        while True:
            counter += 1
            draw = random.sample(range(1, MAX_NUMBER + 1), BALL_COUNT)
            if counter % 100000 == 0:
                 yield f"data: {json.dumps({'counter': counter, 'drawPreview': draw})}\n\n"
            if set(draw) == set(picks):
                total_cost = counter * COST_PER_DRAW
                yield f"data: {json.dumps({'counter': counter,'cost': total_cost,'draw': draw})}\n\n"
                break

    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2137)

