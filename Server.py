import cv2
from flask import Flask
from flask import *

app = Flask(__name__)

camera = cv2.VideoCapture(0)
return_value, image = camera.read()
cv2.imwrite('images\opencv.png', image)
del(camera)

@app.route("/")

def main():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('images\opencv.png', image)
    del(camera)
    return send_file('images\opencv.png')

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug = True)
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('opencv.png', image)
    del(camera)

