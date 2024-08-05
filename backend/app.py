from flask import Flask, jsonify,request
from flask_cors import CORS,cross_origin
import base64
import json
app = Flask(__name__)
CORS(app, resources={r"/*": {
    "origins": "https://easyauth-frontend24.azurewebsites.net",
    "allow_headers": ["Content-Type", "Authorization"],
    "supports_credentials": True
    }})

@app.route('/')
def home():
    return "Hello from the backend: The routes are /public , /private and /token. Token."

@app.route('/token')
def tokenfunc():
    return str(request.headers)

@app.route('/api/user-info')
def user_info():
    # The claims are sent in a header
    claims = request.headers.get('X-MS-CLIENT-PRINCIPAL-NAME')
    if claims:
        return jsonify({
            "claims":str(claims)
        })
    else:
        return jsonify({"error": "Not authenticated"}), 401

@app.route('/public')
@cross_origin()
def publicapi():
    return jsonify({"Message":"Hello from the public endpoint!"})

@app.route('/private')
@cross_origin()
def privateapi():
    return jsonify({"Message":"Hello from the private endpoint!"})

if __name__ == "__main__":
    app.run(debug = True)