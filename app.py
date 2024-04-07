from flask import Flask, render_template, request
from model import calculation
from zip_to_coord import ZipToCoord
import ee
import os

app = Flask(__name__)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "crypto-pulsar-418018-70323bd4b67f.json"

ee.Initialize()
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/result" , methods=["POST"])
def process_form():
    budget=request.form.get('budget')
    location=request.form.get("location")
    landsize=request.form.get("landsize")
    print(location,budget,landsize)
    #changing location to coord
    coord = ZipToCoord(location)
    location,result_value=calculation(budget,coord,landsize)
    return render_template("result.html", location=location, result_value=result_value)
if __name__ == '__main__':
    app.run(debug=True)