from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ip", methods=["GET"])
def index():
    ip_address = request.remote_addr
    return "Requester IP: " + ip_address

@app.route("/ip_public", methods=["GET"])
def public():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return (request.environ['REMOTE_ADDR'])
    else:
        return (request.environ['HTTP_X_FORWARDED_FOR'])

if __name__ == "__main__":
    app.run(debug=True, port=80)
    
#https://www.youtube.com/watch?v=oA8brF3w5XQ&t=840s