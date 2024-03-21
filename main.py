from pathlib import Path

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

ROCK_NAMES = [
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
    return render_template("index.html", rock_names=ROCK_NAMES)


@app.route("/upload", methods=["post"])
def upload():
    file = request.files.get("uploaded-file")
    filename = secure_filename(file.filename)
    file.save(Path("uploads") / filename)
    return "ok"


if __name__ == '__main__':
    app.run()
