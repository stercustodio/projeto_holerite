from flask import Flask

from src.routes.cargo import cargo
from src.routes.funcionario import funcionario

app_ste = Flask(__name__)
app_ste.register_blueprint(funcionario)
app_ste.register_blueprint(cargo)
