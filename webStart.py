from flask import Flask, render_template, request
app = Flask(__name__, static_url_path="/static, /static/css")
import sys
import restaurants.py
import museums.py
import parks.py

@app.route('/')
def index():
    return render_template("landing_page.html")

@app.route('/itinerary')
def itinerary():
    return render_template("query_page.html")

@app.route('/result')
def result():
    return render_template("result_page.html")

@app.route('/handle-form', methods=['POST'])
def registerForm():
    print("Hello")
    if request.method == 'POST':
        return str(request.form)
        #return str(dir(request))
    res=restaurants.restaurantData()
    mus=museums.museumData()
    par=parks.parkData()
    resArr=[]
    musArr=[]
    parArr=[]
    for i in range(0,2):
        resArr.append(res.getRestraunt(Form.get("City")).title())
        musArr.append(mus.getMuseum(Form.get("City")).upper())
        parArr.append(par.getPark(Form.get("State")).upper())

    return "Nothin'"
if __name__ == "__main__":
    app.run()
