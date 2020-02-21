"""
AUTOR: gkvn

DATE CREATION: 21/2/2020

"""
from flask import Blueprint

auth_bp = Blueprint("auth", __name__, template_folder="templates")

from . import routes