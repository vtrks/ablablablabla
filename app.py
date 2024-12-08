from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.context_processor
def inject_time():
    return {"current_time": datetime.now().strftime("%H:%M:%S")}

if __name__ == "__main__":
    app.run(debug=True)

from flask_frozen import Freezer

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()