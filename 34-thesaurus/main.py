from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("disctionary.csv")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def api(word):
    definition= df.loc[df["word"] == word]["definition"].squeeze()
    result_dictionary = {"word": word, "defintion": definition}
    return result_dictionary

if __name == "__main__":
    app.run(debug=True, port=5001)