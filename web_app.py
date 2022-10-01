# from flask import Flask, render_template, jsonify, request

# from chat import get_response, bot_name

# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


# @app.route('/', methods=["GET", "POST"])
# def index():
#     return render_template('templetes/index.html', **locals())


# @app.route('/chatbot', methods=["GET", "POST"])
# def chatbotResponse():

#     if request.method == 'POST':
#         the_question = request.form['question']

#         response = get_response(the_question)

#     return jsonify({"response": response})


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port='8888', debug=True)
