from flask import Flask, request, jsonify
from flask_cors import CORS

from scipy.misc import imsave, imread, imresize
import numpy as np
# import keras.models
# import re

import base64

import sys, os, io
sys.path.append(os.path.abspath('./model'))

# import load as load_model
# global model, graph
# model, graph = load_model.init()

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/predict', methods=['POST'])
def predict():
	formFile = request.files.get('file')
	img = imread(formFile)
	print(img.shape)
	return jsonify({ "len": len(img) })

def predict2():
	# imgData = request.get_data()
	imgData = request.form['img']
	#encode it into a suitable format
	convertImage(imgData)
	print("debug")
	#read the image into memory
	x = imread('output.png',mode='L')
	#make it the right size
	x = imresize(x,(28,28))
	#imshow(x)
	#convert to a 4D tensor to feed into our model
	x = x.reshape(1,28,28,1)
	print("debug2")
	#in our computation graph
	with graph.as_default():
		#perform the prediction
		out = model.predict(x)
		print(out)
		print(np.argmax(out,axis=1))
		print("debug3")
		#convert the response to a string
		response = np.array_str(np.argmax(out,axis=1))
		return response

def convertImage(imgData1):
    imgstr = re.search(b'base64,(.*)',imgData1).group(1)
    with open('output.png','wb') as output:
        output.write(base64.b64decode(imgstr))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=os.environ.get('PORT', 9000))
	#app.run(debug=True)
