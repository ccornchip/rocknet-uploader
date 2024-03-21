import base64
import os
import re
import time
from pathlib import Path

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

ROCK_NAMES_EN = [
    "Granite",
    "Sandstone",
    "Limestone",
    "Schist",
    "Marble",
    "Micaschist",
    "Orthogneiss ",
    "Conglomerate",
    "Gabbro ",
    "Flint",
    "Evaporite",
    "Dunite",
    "Quartzite",
    "Basalt",
    "Trachyte",
    "Meulière stone",
    "Rhyolite ",
    "Diorite ",
    "Obsidian",
    "Tuff",
    "Eclogite",
    "Serpentinite ",
    "Pumice",
    "Peridotite",
    "Andesite",
    "Granodiorite",
    "Coal",
    "Others"]

ROCK_NAMES_FR = [
    "Granite",
    "Grès",
    "Calcaire",
    "Schiste",
    "Marbre",
    "Micaschiste",
    "Orthogneiss",
    "Conglomérat",
    "Gabbro",
    "Silex",
    "Évaporite",
    "Dunite",
    "Quartzite",
    "Basalte",
    "Trachyte",
    "Meulière",
    "Rhyolite",
    "Diorite",
    "Obsidienne",
    "Tuf",
    "Éclogite",
    "Serpentinite",
    "Pierre Ponce",
    "Péridotite",
    "Andésite",
    "Granodiorite",
    "Charbon",
    "Autres",
]


@app.route("/")
@app.route("/index")
def index():
    language = request.values.get("hl", "en")
    rock_names = ROCK_NAMES_EN if language == "en" else ROCK_NAMES_FR
    return render_template("index.html", rock_names=zip(rock_names, ROCK_NAMES_EN))


@app.route("/upload", methods=["post"])
def upload():
    for rock_name in ROCK_NAMES_EN:
        files = request.files.getlist(f"{rock_name}-uploaded-file")
        for file in filter(lambda f: f.filename, files):
            filename = secure_filename(file.filename)
            uid = base64.b64encode(time.time_ns().to_bytes(9, "big"), altchars=b"-_").decode()
            newfilename = re.sub(r'(.*)\.(.*)$', rf'\g<1>-{uid}.\g<2>', filename)
            os.makedirs(Path("uploads") / rock_name, exist_ok=True)
            file.save(Path("uploads") / rock_name / newfilename)
    return "ok"


if __name__ == '__main__':
    app.run()
