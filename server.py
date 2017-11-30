import json
import os

from flask import Flask, render_template, jsonify, request, Response

from Exceptions.InvalidParameter import InvalidParameterException
from Utils.Utila import Utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index")


@app.route('/add/<acronym>', methods=['POST'])
def add(acronym):
    # Validation
    if not acronym:
        raise InvalidParameterException('Parameter missing', status_code=402)
    if not request.data:
        raise InvalidParameterException('Body missing', status_code=402)

    # acronyms.json filepath
    file_path = get_filepath()

    # reads from existing file if not empty, create an empty list [] otherwise
    content = Utils().get_file_content(file_path)
    new_data = json.loads(request.data)

    # assert body integrity
    if not "definition" in new_data or not "version" in new_data:
        raise InvalidParameterException('Missing fields in body, required are [version, definition]', status_code=400)

    # add acronym to "name" field in data
    new_data["name"] = acronym

    ff = open(file_path, "w")
    if new_data in content:
        raise InvalidParameterException(acronym + " already exists. Use HTTP [PATCH] to update existing acronyms",
                                        status_code=400)
    content.append(new_data)

    # writing to file
    ff.write(json.dumps(content))
    ff.close()

    # returning what has been written
    return Response(json.dumps(new_data), status=201, mimetype='application/json')


@app.route('/acronym')
def acronym():
    # traitement
    return dict()


@app.errorhandler(InvalidParameterException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def get_filepath():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "data", "acronyms.json")
    return file_path


if __name__ == "__main__":
    app.run(debug=True)
