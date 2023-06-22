from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/getJson', methods=['POST'])
def get_json():
    data = request.json['inputData']
    response = requests.get(f"https://www.daegufood.go.kr/kor/api/tasty.html?mode=json&addr={data}")
    info = response.json()
    return jsonify(info)
    


if __name__ == '__main__':
    app.run(port=3000)