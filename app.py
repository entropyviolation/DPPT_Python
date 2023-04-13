from flask import Flask, render_template, request, jsonify
import game_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/start', methods=['GET'])
def start_game():
    questions = game_code.get_random_questions()
    return jsonify(questions)

@app.route('/game/follow_up', methods=['POST'])
def follow_up():
    response = request.get_json()
    context = response['context']
    follow_up_question = game_code.generate_follow_up(response['answer'], context)
    return jsonify(follow_up_question)


@app.route('/game/analyze', methods=['POST'])
def analyze():
    responses = request.get_json()
    print("Received responses:", responses)
    analysis = game_code.analyze_responses(responses)
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(debug=True)
