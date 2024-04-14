from flask import Flask, send_file, render_template

app = Flask(__name__)


@app.get("/")
def get_root():
    return {
        "endpoints": {
            "/static": "GET",
            "/server/<data>": "GET",
            "/client": "GET"
        }
            
    }

@app.get("/static")
def get_static():
    return send_file("static.html")

@app.get("/server/<data>")
def get_server(data):
    return render_template("server.html", data=data)

@app.get("/client")
def get_client():
    return send_file("client.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)