"""
References:

https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/
https://stribny.name/blog/2020/07/real-time-data-streaming-using-fastapi-and-websockets/
"""

import datetime
from typing import Generator

import cv2
import threading
import time

from app.conf.logger import logger


class TrumanCamera:
    thread = None

    def __init__(self, fps=20, video_source=0):
        logger.info(f"Initializing camera class with {fps} fps and video_source={video_source}")
        self.fps = fps
        self.video_source = video_source  # TODO: Select camera available from OS
        self.camera = cv2.VideoCapture(self.video_source)
        # We want a max of 5s history to be stored, thats 5s*fps
        self.max_frames = 5 * self.fps
        self.frames = []
        self.isrunning = False

    @staticmethod
    def _get_camera_from_os(self) -> cv2.VideoCapture:
        devices = 4
        for device in range(devices):
            camera = cv2.VideoCapture(f'/dev/video{device}')
            if camera:
                logger.info(f'Camera {device} selected.')
                break
            else:
                logger.error('Camera found')
        return camera

    def run(self):
        logger.debug("Perparing thread")
        if self.thread is None:
            logger.debug("Creating thread")
            thread = threading.Thread(target=self._capture_loop, daemon=True)
            logger.debug("Starting thread")
            self.isrunning = True
            thread.start()
            logger.info("Thread started")

    def _capture_loop(self):
        dt = 1 / self.fps
        logger.debug("Observation started")
        while self.isrunning:
            ret, img = self.camera.read()
            if ret:
                if len(self.frames) == self.max_frames:
                    self.frames = self.frames[1:]
                self.frames.append(img)
            time.sleep(dt)
        logger.info("Thread stopped successfully")

    def stop(self):
        logger.debug("Stopping thread")
        self.isrunning = False

    # def get_frame(self, _bytes=True):
    #     if len(self.frames) > 0:
    #         if _bytes:
    #             img = cv2.imencode('.png', self.frames[-1])[1].tobytes()
    #         else:
    #             img = self.frames[-1]
    #     else:
    #         with open("images/not_found.jpeg", "rb") as f:
    #             img = f.read()
    #     return img

    def gen_frames(self) -> Generator:
        logger.debug('Sending frames')
        while True:
            success, frame = self.camera.read()
            if not success:
                logger.error('No camera found.')
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        self.camera.release()
