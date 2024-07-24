from flask import Flask, send_file, jsonify, abort, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Image API")

@app.route('/image')
def get_image():
    filename = request.args.get('filename', default="example.jpg")
    if not os.path.isfile('static/images/'+filename):
        abort(404, description="Image not found")
    
    return send_file('static/images/'+filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
