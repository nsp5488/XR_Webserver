from flask import Blueprint, send_from_directory, redirect, url_for, render_template, request, current_app
import os
from convert_pdf import convert_and_save

blueprint = Blueprint("route_blueprints", __name__)


@blueprint.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/<value>')
def success(value):
    return render_template('index.html', folder_name=value)


@blueprint.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        new_folder = convert_and_save(uploaded_file.filename)
        return redirect(url_for('route_blueprints.success', value=new_folder))
    return redirect(url_for('route_blueprints.index'))


@blueprint.route('/uploads/<folder>')
def upload(folder):
    index = request.args.get("index")
    if index is not None:
        return send_from_directory(os.path.join(current_app.config['UPLOAD_PATH'], folder), f"{index}.jpg")

    items = len(os.listdir(os.path.join(
        current_app.config['UPLOAD_PATH'], folder)))
    return {"slides": items}
