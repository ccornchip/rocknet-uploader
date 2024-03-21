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
    return render_template("index.html", rock_names=rock_names)


@app.route("/upload", methods=["post"])
def upload():
    file = request.files.get("uploaded-file")
    filename = secure_filename(file.filename)
    file.save(Path("uploads") / filename)
    return "ok"


if __name__ == '__main__':
    app.run()
