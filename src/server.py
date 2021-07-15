from flask import Flask
from random_word import RandomWords

words = RandomWords()
server = Flask(__name__)
word = words.get_random_word()


@server.route("/")
def hello():
    return f'<h1>{word}</h1>'


if __name__ == "__main__":
    print('******************\n', word, '******************\n')
    server.run(host='0.0.0.0')
