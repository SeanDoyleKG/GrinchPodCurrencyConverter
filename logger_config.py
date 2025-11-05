import logging


def setup_logging():
    logger = logging.getLogger("currency_converter")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler("converter.log")
        sh = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(sh)

    return logger


if __name__ == "__main__":
    print("=== Testing Logger Config ===")

    logger = setup_logging()

    logger.debug("This is a DEBUG message - should NOT appear")
    logger.info("This is an INFO message - should appear")
    logger.warning("This is a WARNING message - should appear")
    logger.error("This is an ERROR message - should appear")
    logger.critical("This is a CRITICAL message - should appear")

    print("=== Logger Test Complete ===")
    print("Check both console output and converter.log file!")
