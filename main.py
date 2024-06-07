import base64
import os
import time
from datetime import timedelta
from pathlib import Path

from flask import Flask, request, render_template, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)

ROCK_NAMES_EN = [
    "Conglomerate",
    "Spilite",
    "Limestone",
    "Pellite (Schiste)",
    "Sandstone",
]

ROCK_NAMES_FR = [
    "Conglomérat",
    "Spilite",
    "Calcaire",
    "Pellite (Schiste)",
    "Grès",
]


@app.route("/")
@app.route("/index")
def index():
    language = request.cookies.get("hl", "en")
    language = request.values.get("hl", language)
    rock_names = ROCK_NAMES_EN if language == "en" else ROCK_NAMES_FR
    response = make_response(render_template("index.html",
                                             rock_names=zip(rock_names, ROCK_NAMES_EN),
                                             hl=language))
    response.set_cookie("hl", language, max_age=timedelta(weeks=52))
    return response


@app.route("/upload", methods=["post"])
def upload():
    language = request.cookies.get("hl", "en")
    language = request.values.get("hl", language)
    for rock_name in ROCK_NAMES_EN:
        files = request.files.getlist(f"{rock_name}-uploaded-file")
        for file in filter(lambda f: f.filename, files):
            filename = secure_filename(file.filename)
            uid = base64.b64encode(time.time_ns().to_bytes(9, "big"), altchars=b"-_").decode()
            splitname = filename.rsplit(".", maxsplit=1)
            newfilename = f"{splitname[0]}-{uid}"
            if len(splitname) == 2:
                newfilename += f".{splitname[1]}"
            os.makedirs(Path("uploads") / rock_name, exist_ok=True)
            file.save(Path("uploads") / rock_name / newfilename)
    return render_template("success.html", hl=language)


if __name__ == '__main__':
    app.run()
