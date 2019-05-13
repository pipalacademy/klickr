import web
from klickr import config

db = web.database(config.DATABASE_URL)

with open('klickr/schema.sql') as f:
    schema = f.read()

db.query(schema)
