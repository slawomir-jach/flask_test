from flask import Flask
from flask import jsonify
from flask import request
from flask import Response

app = Flask(__name__)


@app.after_request
def treat_as_plain_text(response):
    response.headers["content-type"] = "text/plain"
    return response

@app.route("/ip", methods=["GET"])
def ip():
   return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
#    return jsonify({'ip': request.remote_addr}), 200



@app.route("/")
def index():
    return "<h3 > Hello Nokia <h3/>"




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
