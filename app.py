#!python3

import os
import json
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def root():
    DATABASE_URL = os.environ['DATABASE_URL']
    dbconn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = dbconn.cursor()
    cursor.execute("""SELECT
      id, sfid, firstname, lastname, email, createddate
      FROM
      salesforce.contact
      ORDER BY
      systemmodstamp DESC;""")
    records = cursor.fetchall()

    res = make_response(json.dumps(records, default=str))
    res.mimetype = 'application/json'
    return res

    #res = ""
    #for row in records:
    #    res = res + "[ "
    #    for column in row:
    #        res = res + str(column) + " | "
    #    res = res + "]\n"

    #return res
