from flask import Flask, render_template, request
app = Flask(__name__, static_url_path="/static, /static/css")

@app.route('/')
def index():
    return render_template("landing_page.html")

@app.route('/itinerary')
def itinerary():
    return render_template("query_page.html")

@app.route('/result')
def result():
    return render_template("result_page.html")

if __name__ == "__main__":
    app.run()
