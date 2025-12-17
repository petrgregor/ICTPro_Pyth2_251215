import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="example.log",
    filemode='a'
)

logger = logging.getLogger(__name__)

logger.debug("This is DEBUG info.")
logger.info("This is INFO log.")
logger.warning("This is WARNING.")
logger.error("This is ERROR.")
logger.critical("This is critical.")
