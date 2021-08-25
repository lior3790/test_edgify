# #!/usr/bin/env python3

# from flask import Flask
# app = Flask(__name__)

# import connexion

# from swagger_server import encoder

# @app.route("/")
# def main():
#     app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
#     app.app.json_encoder = encoder.JSONEncoder
#     app.add_api('swagger.yaml', arguments={'title': 'Swagger Edgify Trading'}, pythonic_params=True)
#     app.run(port=8080)