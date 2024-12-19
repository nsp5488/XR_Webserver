from flask import Blueprint, send_from_directory, redirect, url_for, render_template, request, current_app, abort
import os
from convert_pdf import convert_and_save, get_current_uploads, delete_folder, sterilize_path
from werkzeug.utils import secure_filename

blueprint = Blueprint("route_blueprints", __name__)

@blueprint.route('/')
def index():
    return render_template('home.html')


@blueprint.route('/<value>')
def success(value):
    path = os.path.join(current_app.config['UPLOAD_PATH'], value)
    cleaned_path = sterilize_path(path, current_app.config['UPLOAD_PATH'])
    if cleaned_path is not None and os.path.exists(path):
        return render_template('home.html', folder_name=value)
    else:
        return redirect(url_for('route_blueprints.index'))
        
@blueprint.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(current_app.root_path, 'static'),
                               'images/favicon.png', mimetype='image/vnd.microsoft.icon')
@blueprint.route("/about")
def about():
    return render_template('about.html')


@blueprint.route('/help')
def help():
    # Render the Help page with a large text area
    return render_template('help.html')

@blueprint.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Handle form submission for Admin page
        string_input = request.form['string_input']
        if string_input == current_app.config["ADMIN_PASSWORD"]:
            presentations = get_current_uploads(current_app.config['UPLOAD_PATH'], current_app.config['VALID_EXTENSIONS'])
            return render_template('admin.html', presentations=presentations, delete_id=current_app.config['DELETE_IDENTIFIER'])
    # Render the Admin page with the form
    return render_template('admin.html')

@blueprint.route('/delete', methods=["POST"])
def delete():
    # Ensure that this request is authenticated properly
    if request.form['form_identifier'] != current_app.config['DELETE_IDENTIFIER']:
        abort(401)
    code = request.form['code']
    delete_folder(current_app.config['UPLOAD_PATH'], code)
    presentations = get_current_uploads(current_app.config['UPLOAD_PATH'], current_app.config['VALID_EXTENSIONS'])
    return render_template('admin.html', presentations=presentations, delete_id=current_app.config['DELETE_IDENTIFIER'])



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
        current_app.config['UPLOAD_PATH'], folder))) - 1 # remove 1 for the metadata file
    return {"slides": items}
