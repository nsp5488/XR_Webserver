from flask import Blueprint, send_from_directory, redirect, url_for, render_template, request, current_app, abort
import os
from convert_pdf import convert_and_save
from werkzeug.utils import secure_filename

blueprint = Blueprint("route_blueprints", __name__)

@blueprint.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/<value>')
def success(value):
    path = os.path.join(current_app.config['UPLOAD_PATH'], value)
    if os.path.exists(path):
        return render_template('index.html', folder_name=value)
    else:
        return redirect(url_for('route_blueprints.index'))


@blueprint.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        # handle security checks on file.
        filename = secure_filename(uploaded_file.filename)
        file_extension = os.path.splitext(filename)[1]
        if file_extension not in current_app.config["VALID_EXTENSIONS"]:
            abort(400)

        # save the file, convert it to images, then remove the file to free up storage.
        uploaded_file.save(os.path.join(current_app.config["UPLOAD_PATH"], filename))
        new_folder = convert_and_save(filename, current_app.config["UPLOAD_PATH"])
        os.remove(os.path.join(current_app.config["UPLOAD_PATH"], filename))


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
