from matplotlib.style import available
from pycalphad import Database
from requests import get
from flask import jsonify, app, get, post, request
import os

db = []

@app.get('/database')
def check_database():
    for filename in os.listdir("../databases"):
       db.append(filename)
    available_bases = db
    name_of_db = request.get('database')
    if name_of_db in available_bases:
        currentdb = Database("/databases" + name_of_db)
        elements = list(currentdb.elements)
        for i in range(0, len(elements)):
            if elements[i] == "VA" or elements[i] == "/":
                elements.pop(i)
        return jsonify({
        'elements': elements,
        'db': currentdb,
        })
    else:
        return jsonify({'error': 'This database is currently unavailable'})






        
        