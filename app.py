#!python3

import os
from flask import Flask, jsonify
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def root():
    DATABASE_URL = os.environ['DATABASE_URL']
    dbconn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = dbconn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("""SELECT
      id, sfid, firstname, lastname, email, createddate
      FROM
      salesforce.contact
      ORDER BY
      systemmodstamp DESC;""")
    records = cursor.fetchall()

    return jsonify(records)
