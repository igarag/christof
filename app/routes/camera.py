# import io
# from starlette.responses import StreamingResponse

from fastapi import APIRouter, Response

from app.conf.settings import logger
from app.services.security_webcam import TrumanCamera

router = APIRouter(
    prefix=""
)


@router.get('/video-feed')
def video_feed() -> Response:
    logger.debug(f'Sending frames')
    headers = {'mimetype': 'multipart/x-mixed-replace; boundary=frame'}
    return Response(TrumanCamera.gen_frames(), headers=headers)


# @app.post("/vector-image")
# def image_endpoint(*, vector):
#     # Returns a cv2 image array from the document vector
#     cv2img = my_function(vector)
#     res, im_png = cv2.imencode(".png", cv2img)
#     return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")
