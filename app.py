from flask import Flask, render_template, request
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

app = Flask(__name__, template_folder='static/html', static_folder='static')

bot = ChatBot("Sara", storage_adapter="chatterbot.storage.SQLStorageAdapter")

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python','gustavo','é um palhaço']
bot.set_trainer(ListTrainer)
bot.train(conversa)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/getresponse")
def get_bot_response():
    nresponse = "IDN"
    userText = request.args.get('msg')
    response = bot.get_response(userText)
    if float(response.confidence) > 0.5:
        return str(response)
    else:
        return str(nresponse)

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run()
