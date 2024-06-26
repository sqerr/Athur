from flask import Flask, jsonify, url_for, send_file
import os
from flask_cors import CORS
from PIL import Image
import base64
app = Flask(__name__)
CORS(app)


@app.route('/entry')
def entry_return():
    test = {'test': 123}
    return jsonify(test)


CORS(app)


@app.route('/img')
def get_img():
    return send_file("1.jpg")

@app.route('/slider')
def get_url_for_slider():
    return jsonify(os.listdir('slider'))

@app.route('/get_img/<test>')
def get_img_for_src(test):
    return send_file(f'slider/{test}')

if __name__ == '__main__':
    app.run(debug=True)
