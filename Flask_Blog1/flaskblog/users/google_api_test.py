import os
import io
import cv2
from google.cloud import vision
from google.cloud.vision import types

export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"



def recognize_license_plate(img_path):
	start_time = datetime.now()

	img = cv2.imread(img_path)

	height, width = img.shape[:2]

	img = cv2.resize(img, (800, int((height * 800)/width)))

	cv2.imshow("S")

	client = vision.ImageAnnotatorClient()

	with io.open(img_path, 'rb') as image_file:
		content = image_file.read()

		




























