from typing import Generator
import cv2
from fastapi import APIRouter
from fastapi.responses import StreamingResponse, Response

from app.conf.logger import logger
from app.services.security_webcam import TrumanCamera

router = APIRouter(
    prefix=""
)


truman = TrumanCamera()
truman.run()


def generate_frames() -> Generator:
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            logger.error('No camera found.')
            break
        else:
            ret, img = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                   bytearray(img) + b'\r\n')
    camera.release()


@router.get('/video-feed')
def video_feed() -> StreamingResponse:
    logger.debug(f'Sending images . . .')
    return StreamingResponse(truman.gen_frames(),
                             media_type="multipart/x-mixed-replace;boundary=frame")


@router.get('/video-stop')
def video_feed() -> Response:
    logger.debug(f'Stopping video.')
    return Response(truman.stop(), )
