from flask import Flask, render_template, request
from model import calculation
from zip_to_coord import ZipToCoord
##import ee
import os

app = Flask(__name__)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "crypto-pulsar-418018-70323bd4b67f.json"

##ee.Initialize()
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/result" , methods=["POST"])
def process_form():
    location=str(request.form.get("location"))
    landsize=str(request.form.get("landsize"))
    irrigation_water, suggested_crop, estimated_costs, irrigation_costs, material_cost, total_yield, income = calculation(location,landsize)
    return render_template("result.html", location=location, irrigation_water=irrigation_water, suggested_crop=suggested_crop, estimated_costs=estimated_costs, irrigation_costs=irrigation_costs, material_cost=material_cost, total_yield=total_yield, income=income)

if __name__ == '__main__':
    app.run(debug=True)