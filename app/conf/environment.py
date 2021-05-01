from environs import Env

env = Env()
env.read_env()

# Logger
LOG_FILE = env.str("LOG_FILE", "app.log")
LOGGER_NAME = env.str("LOGGER_NAME", "model-deployment-manager")
JSON_LOGGER = env.bool("JSON_LOGGER", True)
JSON_LOGGER_INDENT = env.int("JSON_LOGGER_INDENT", 4)
