import logging

from klickr.app import app, db

def setup_logger(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(message)s",
        datefmt="%H:%M:%S"
    )

def create_tables():
    schema = open('klickr/schema.sql').read()
    db.query(schema)

def main():
    setup_logger(verbose=True)
    create_tables()
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
