
### Simple API return data using GET variable

## Pre-requisites
# kena isntall flask (Python web framework)
# run "python -m pip install flask" untuk install flask

## Cara pakai
# access http://127.0.0.1:5000/data
# define GET variable name, example http://127.0.0.1:5000/data?name=asyraf
# return result based on data


###########################################################################
## Data - reading dari database/person.json##

import json

# Open and read JSON file
with open("database/person.json", "r", encoding="utf-8") as file:
    people = json.load(file)

## Handling request ##
from flask import Flask, request

app = Flask(__name__)

@app.route('/data') # yang ni define URL path
def home():
        keyword = request.args.get('name') 

        if keyword is None:
            return "No name provided!"
        elif keyword in people:
            return people[keyword]
        else:
            return "Data not found!"
            
if __name__ == '__main__':
    app.run(debug=True)

###########################################################################