from flask import Blueprint

query = Blueprint('questions' , __name__)

from app.questions import routes