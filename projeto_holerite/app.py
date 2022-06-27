from flask import Flask

from src.routes.cargo import cargo
from src.routes.funcionario import funcionario

app = Flask(__name__)
app.register_blueprint(funcionario)
app.register_blueprint(cargo)
