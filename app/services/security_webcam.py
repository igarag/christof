"""
References:

https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/
https://stribny.name/blog/2020/07/real-time-data-streaming-using-fastapi-and-websockets/
"""

import datetime
from typing import Generator

import cv2

from app.conf.settings import logger


class TrumanCamera:
    def get_camera_from_os(self) -> cv2.VideoCapture:

        devices = 4
        for device in range(devices):
            camera = cv2.VideoCapture(f'/dev/video{device}')
            if camera:
                logger.info(f'Camera {device} selected.')
                break
            else:
                logger.error('Camera found')
        return camera

    def __init__(self):
        self.camera = self.get_camera_from_os()
        self.total = 70

    def gen_frames(self) -> Generator:
        while True:
            success, frame = self.camera.read()
            if not success:
                logger.error('No camera found.')
                break
            else:
                logger.info('Sending frames')
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        self.camera.release()
