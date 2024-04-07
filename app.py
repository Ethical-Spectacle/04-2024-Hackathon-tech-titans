from flask import Flask, render_template, request
from model import calculation

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/result" , methods=["POST"])
def process_form():
    budget=request.form.get('budget')
    location=request.form.get("location")
    landsize=request.form.get("landsize")
    print(location,budget,landsize)
    location,result_value=calculation(budget,location,landsize)
    return render_template("result.html", location=location, result_value=result_value)