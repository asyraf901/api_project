
### Simple API return data using GET variable

## Pre-requisites
# kena isntall flask (Python web framework)
# run "python -m pip install flask" untuk install flask

## Cara pakai
# access http://127.0.0.1:5000/data
# define GET variable name, example http://127.0.0.1:5000/data?name=asyraf
# return result based on data


###########################################################################

from flask import Flask, request, jsonify
app = Flask(__name__)

### Variable ###
API_KEY = "acapPalingHensem"

### Check API key dari header ###

@app.before_request
def check_api_key():
    key = request.headers.get("X-API-KEY")
    print(f"key")
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

### Data - reading dari database/person.json ###

import json

# Open and read JSON file
with open("database/person.json", "r", encoding="utf-8") as file:
    people = json.load(file)

### Handling request ###

@app.route('/data', methods=['POST']) # yang ni define URL path
def home():
        data = request.get_json()
        keyword = data.get("name")

        if keyword is None:
            return "No name provided!"
        elif keyword in people:
            return people[keyword]
        else:
            return "Data not found!"
            
if __name__ == '__main__':
    app.run(debug=True)

###########################################################################