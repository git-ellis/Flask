from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:/Python/workspaces/Flask/flaskr/apps/upload'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 7.5  # 7.5MB
upload_folder = app.config['UPLOAD_FOLDER']


@app.route("/")
def index():
    return render_template("file_upload.html")


@app.route("/upload", methods=['POST'])
def upload():
    files = request.files
    f = files.get("file")
    print(f, dir(f))
    print(f"name = {f.name}")
    print(f"filename = {f.filename}")
    print(f"secure_filename(f.filename) = {secure_filename(f.filename)}")
    print(f"content_type = {f.content_type}")
    print(f"content_length = {f.content_length}")
    print(f"headers = {f.headers}")
    print(f"mimetype = {f.mimetype}")
    print(f"mimetype_params = {f.mimetype_params}")

    filename = secure_filename(f.filename)
    f.save(os.path.join(upload_folder, filename))

    return redirect(url_for("show_uploaded_file", filename=filename))


@app.route("/show_uploaded_file/<filename>", methods=['GET', 'POST'])
def show_uploaded_file(filename):
    return send_from_directory(upload_folder, filename)


if __name__ == '__main__':
    app.run(debug=True)
