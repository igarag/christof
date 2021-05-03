import logging

from pythonjsonlogger import jsonlogger

from app.conf.environment import LOG_FILE, LOGGER_NAME, JSON_LOGGER, JSON_LOGGER_INDENT

logger = logging.getLogger(LOGGER_NAME)
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename=f"/tmp/{LOG_FILE}", mode='w')

if JSON_LOGGER:
    formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d] %(name)s',
        json_indent=JSON_LOGGER_INDENT
    )
else:
    formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s')

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.setLevel(level=logging.DEBUG)
logger.propagate = False
