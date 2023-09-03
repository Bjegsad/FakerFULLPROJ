from flask import render_template
from flask import Flask
from flask import request

from model import nlp

from news_parser import parser

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    label_dict = {'LABEL_0': False, 'LABEL_1': True}
    if request.method == "GET":
        return render_template("index.html", value=True)
    if request.method == "POST":
        message = request.form.to_dict()
        value = parser(message['message'])
        if value is None:
            return render_template("index.html", value=False)
        else:
            processed_text = nlp(value)[0]
            precision_score = str(round(processed_text['score'] * 100, 2)) + "%"
            label = processed_text['label']
            return {'label': label_dict[label],
                    'score': precision_score} #render_template("index.html", label=label_dict[label], score=precision_score)


if __name__ == "__main__":
    app.run(debug=True)
