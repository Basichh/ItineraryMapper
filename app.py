# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/itinerary')
def itinerary():
    city = request.args.get('city')
    # Here you would normally process the city to generate an itinerary.
    # For demonstration purposes, we'll just pass the city to the template.
    return render_template('itinerary.html', city=city)

if __name__ == '__main__':
    app.run(debug=True)
