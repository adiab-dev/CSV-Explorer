import uuid
from io import BytesIO
from flask import Flask, render_template, request, send_file, abort

app = Flask(
    __name__,
    template_folder='../frontend',
    static_folder='../frontend',
    static_url_path='/static'
)

uploads = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    print("received upload request")
    print("files", request.files)
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            return 'No file selected', 400
        if not file.filename.lower().endswith('.csv'):
            return 'Only CSV files are allowed', 400
        file_id = str(uuid.uuid4())

        uploads[file_id] = {
            'filename': file.filename,
            'data': file.read()
        }
        return render_template('index.html', download_id = file_id)
    return render_template('index.html')

@app.route('/download/<file_id>')
def download(file_id):
    upload = uploads.get(file_id)
    if not upload:
        abort(404)
    return send_file(
        BytesIO(upload['data']),
        download_name=upload['filename'],
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)