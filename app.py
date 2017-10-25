from flask import Flask, request, jsonify
from flask_cors import CORS

from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models

import sys, os
sys.path.append(os.path.abspath('./model'))

import load as load_model
global model, graph
model, graph = load_model.init()

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

def generate_input_image(img_array):
	img_resized = imresize(img_array, (480, 480))
	imsave('resized.jpg', img_resized)
	X = img_resized.reshape(1, 480, 480, 3)
	X = X/255.0
	return X

@app.route('/', methods=['GET'])
def frontpage():
	return 'Hi. This is the backend-server for deep-shrooms'

@app.route('/predict', methods=['POST'])
def predict():
	if 'multipart/form-data' not in request.headers['Content-Type']:
		return "Content-Type wasn't 'multipart/form-data'", 400
	try:
		formFile = request.files['file']
	except:
		return "FormData didn't include a file", 400
	try:
		img = imread(formFile)
	except:
		return 'Unable to read the image file', 400

	print(img.shape)
	X = generate_input_image(img)
	with graph.as_default():
		prediction = model.predict(X)
		print(prediction)
		pred_value = prediction.flatten().tolist()[0]
		return jsonify({ "prediction": pred_value })

if __name__ == "__main__":
	app.run(host='localhost', port=os.environ.get('PORT', 9000))
