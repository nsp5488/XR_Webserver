from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from convert_pdf import convert_and_save
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        new_folder = convert_and_save(uploaded_file.filename)
        return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route('/uploads/<folder>')
def upload(folder):
    index = request.args.get("index")
    if index is not None:

        return send_from_directory(os.path.join(app.config['UPLOAD_PATH'], folder), f"{index}.jpg")

    items = len(os.listdir(os.path.join(app.config['UPLOAD_PATH'], folder)))
    return {"slides": items}


if __name__ == '__main__':
    app.config['UPLOAD_PATH'] = 'uploads'
    app.run()
