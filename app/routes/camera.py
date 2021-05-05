# import io
# from starlette.responses import StreamingResponse

from typing import Generator
import cv2
from fastapi import APIRouter, Response

from app.conf.settings import logger
from app.services.security_webcam import TrumanCamera

router = APIRouter(
    prefix=""
)


def gen_frames():
    camera = cv2.VideoCapture(f'0')
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
    camera.release()


@router.get('/video-feed')
def video_feed() -> Response:
    logger.debug(f'Sending frames')
    headers = {'mimetype': 'multipart/x-mixed-replace; boundary=frame'}
    return Response(gen_frames(), headers=headers)


# @app.post("/vector-image")
# def image_endpoint(*, vector):
#     # Returns a cv2 image array from the document vector
#     cv2img = my_function(vector)
#     res, im_png = cv2.imencode(".png", cv2img)
#     return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")
