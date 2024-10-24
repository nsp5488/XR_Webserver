from flask import Flask
from route_blueprints import blueprint


def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_PATH'] = 'uploads'
    app.config["VALID_EXTENSIONS"] = ['.pdf']
    
    app.register_blueprint(blueprint)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
