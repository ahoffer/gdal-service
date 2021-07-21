import os
from datetime import datetime


from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

server = Flask(__name__)
strtimestamp = datetime.now().isoformat()

# @server.route("/")
def hello():
    return f'<h1>{strtimestamp}</h1>'

@server.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        with open("/tmp/output_file", "bw") as f:
            chunk_size = 4096
            while True:
                chunk = request.stream.read(chunk_size)
                if len(chunk) > 0:
                    f.write(chunk)
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(server.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('download_file', name=filename))
            return file.filename
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# Download from provided URL.
# @server.route('/<path:url>')
# def download(url):
    # req = requests.get(url, stream=True)
    # return Response(stream_with_context(req.iter_content()), content_type=req.headers['content-type'])

def upload(stream, fname):
    with open("/tmp/output_file", "bw") as f:
        chunk_size = 4096
        while True:
            chunk = stream.read(chunk_size)
            if len(chunk) == 0:
                return
            f.write(chunk)


@server.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(server.config["UPLOAD_FOLDER"], name)

if __name__ == "__main__":
    # server.config['UPLOAD_FOLDER'] = '/home/aaron/Downloads'
    server.config['UPLOAD_FOLDER'] = '/app/test_data'
    server.run(host='0.0.0.0')
