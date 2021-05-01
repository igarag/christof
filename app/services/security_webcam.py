"""
References:

https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/
https://stribny.name/blog/2020/07/real-time-data-streaming-using-fastapi-and-websockets/
"""

import datetime
from typing import Generator

import cv2

from app.conf.settings import logger

cam = cv2.VideoCapture('/dev/video2')

total = 70
current = 0

ret, frame = cam.read()

tic = datetime.datetime.now()

camera = cv2.VideoCapture(0)


def get_camera_from_os():
    devices = 4
    for device in range(devices):
        camera = cv2.VideoCapture(f'/dev/video{device}')

        if camera != None:
            logger.info(f'Camera {device} selected.')
            break
        else:
            logger.error('No camera found')
    return camera


def gen_frames() -> Generator:
    while True:
        success, frame = camera.read()
        if not success:
            logger.error('No camera found.')
            break
        else:
            logger.info('Sending frames')
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


while True:
    if current >= total:
        ret, frame = cam.read()
        cv2.imshow('frame', frame)
        if (datetime.datetime.now() - tic) > datetime.timedelta(seconds=1):
            tic = datetime.datetime.now()
        current = 0
    current += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
