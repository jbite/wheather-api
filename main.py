from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}

if name == "__name__":
app.run(debug=True)
