from flask import Flask, jsonify, render_template,make_response, request, send_from_directory

app = Flask(__name__)
@app.route('/')  # index
def index():
    return render_template("index.html")

@app.route("/map/<x>/<y>/<z>",methods=["GET"])
def push_map(x,y,z):
    try:
        image_data = open(f"./map/{z}/{x}_{y}.png", "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
    except:
        image_data = open(f"./map/4/2_5.png", "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="7001")