from flask import Flask, render_template, request
app = Flask(__name__, static_url_path="/static, /static/css")
import sys
import restaurants.py
import museums.py


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
        res=restaurants.restaurantData()
        mus=museums.museumData()
        resArr=[]
        musArr=[]
        for i in range(0,2):
            resArr.append(res.getRestraunt(request.form.get("City")).title())
            musArr.append(mus.getMuseum(request.form.get("City")).upper())
        return str(request.form)
        #return str(dir(request))
    

    return "Nothin'"
if __name__ == "__main__":
    app.run()
