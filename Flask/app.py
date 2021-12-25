from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ip", methods=["GET"])
def index():
    ip_address = request.remote_addr
    #print(request.headers['X-Forwarded-For'])
    #return "Requester IP: " + ip_address
    return request.access_route[-1]

@app.route("/ip_public", methods=["GET"])
def public():
    
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return (request.environ['REMOTE_ADDR'])
    else:
        return (request.environ['HTTP_X_FORWARDED_FOR'])
    
if __name__ == "__main__":
    app.run(debug=True, port=8089)
    
#https://www.youtube.com/watch?v=oA8brF3w5XQ&t=840s
#https://esd.io/blog/flask-apps-heroku-real-ip-spoofing.html
