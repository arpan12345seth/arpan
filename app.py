from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/resume')
def download_resume():
    return send_from_directory('.', 'Arpan_Seth_Resume.pdf', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
