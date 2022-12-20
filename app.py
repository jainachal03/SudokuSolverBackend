from flask import Flask
from flask import request, jsonify

from PIL import Image

from flask_cors import CORS

# from  import CORS
from sudukoMain import process

import numpy as np 

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET', 'POST'])
def home():
    return "Hello, Flask!"

@app.route("/upload", methods = ['POST'])
def upload():
    print("inside upload")
    file = request.files['files']
    img = np.asarray(Image.open(file.stream), dtype=np.uint8)
    # print(img.shape)
    # print(img.shape)
    res = process(img)
    # print("res = ", res)
    print(len(res))
    board = []
    
    for i in range(len(res)):
        lst = res[i].tolist()
        board.append(lst)

    answer = {"board":board}
    return jsonify(answer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)