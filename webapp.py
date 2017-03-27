from flask import Flask, render_template, request, jsonify
import amadeus_api
import os
app = Flask(__name__)

@app.route("/")
def index():
    airport = None
    data = None
    airport = request.values.get('airport')
    data = amadeus_api.autocomp(airport)
    return render_template('index.html', airport=airport, data=data)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
