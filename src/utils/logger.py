import logging

def get_logger(name):

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger(name)


if __name__ == "__main__":

    logger = get_logger(__name__)

    logger.info("Logger initialized")