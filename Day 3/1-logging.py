import logging

logging.basicConfig(level = logging.DEBUG)
logging.debug("Variable value = 25")

logging.basicConfig(level = logging.INFO)
logging.info("This is an info message.")
logging.error("Error message")

logging.basicConfig(level = logging.CRITICAL)
logging.critical("Critical message.")

logging.basicConfig(level = logging.WARNING)
logging.critical("Warning message.")

