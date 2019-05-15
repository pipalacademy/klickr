import logging

from klickr.app import app

def setup_logger(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(message)s",
        datefmt="%H:%M:%S"
    )

if __name__ == '__main__':
    setup_logger(verbose=True)
    app.run(host='0.0.0.0')
