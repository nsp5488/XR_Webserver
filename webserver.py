from flask import Flask
from route_blueprints import blueprint
import os

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_PATH'] = os.getenv("UPLOAD_PATH")
    app.config["VALID_EXTENSIONS"] = ['.pdf']
    app.config['DELETE_IDENTIFIER'] = os.getenv("DELETE_IDENTIFIER")
    app.config["ADMIN_PASSWORD"] = os.getenv("ADMIN_PASSWORD")

    app.register_blueprint(blueprint)
    return app


if __name__ == '__main__':
    app = create_app()
    # if running locally, use the local uploads folder
    app.config['UPLOAD_PATH'] = 'uploads' 
    app.config['DELETE_IDENTIFIER'] = 'delete123'
    app.config["ADMIN_PASSWORD"] = "password"
    app.run()
