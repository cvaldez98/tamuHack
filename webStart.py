from flask import Flask, render_template, request
app = Flask(__name__, static_url_path="/static, /static/css")
import sys
# import readRestaurantsCSV.py
import readMuseumCSV.py
import readPark.py

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
    return "Nothin'"
if __name__ == "__main__":
    app.run()
