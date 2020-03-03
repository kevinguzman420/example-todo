"""
AUTOR. Gkvn

GLORY TO: ¡My Father GOD for helping me in everything!

DATE CREATION: 21/02/2020
"""

from flask import send_from_directory
from app import create_app
import os

# settings_module = os.getenv("APP_SETTINGS_MODULE")
# app = create_app(settings_module)

# @app.route("/media/posts/<filename>")
# def media_posts(filename):
#     dir_path = os.path.join(app.config["MEDIA_DIR"], app.config["POSTS_IMAGES_DIR"])
#     return send_from_directory(dir_path, filename)

app = create_app()
# cli = FlaskGroup(create_app())
# @cli.command("recreate_db")
# def recreate_db():
#     db.drop_all()
#     db.create_all()


#                                   .:START HERE:.
# ESTOY ESTUDIANDO EL TUTORIAL, EN EL CUAL ME QUEDÉ EN LA LECCIÓN 7
# https://j2logo.com/tutorial-flask-leccion-7-parametros-de-configuracion-proyecto/
# TAMBIEN ESTOY TRATANDO DE QUE EL NOMBRE DEL USUARIO APARAZCA EN EL NAVBAR Y EN EL HISTORIAL DE TAREAS REALIZADAS/BORRADAS.