"""
    Initialized server with Flask
"""

from flask import Flask

app = Flask(__name__)

# para rodar servidores em Flask, é preciso definir a função main
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
