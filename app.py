from flask import Flask, render_template, request
from model import calculation

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/result" , methods=["POST"])
def process_form():
    location=str(request.form.get("location"))
    landsize=str(request.form.get("landsize"))
    irrigation_type, suggested_crop, estimated_costs = calculation(location,landsize)
    return render_template("result.html", location=location, irrigation_type=irrigation_type, suggested_crop=suggested_crop, estimated_costs=estimated_costs)

if __name__ == '__main__':
    app.run(debug=True)