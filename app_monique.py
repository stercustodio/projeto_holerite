from flask import Flask

from src.routes.funcionarios import funcionarios

app = Flask(__name__)
app.register_blueprint(funcionarios)
