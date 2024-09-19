from flask import Flask, render_template
from src.constants import ROOT_DIR
import configparser

app = Flask(__name__)


def parse_config():
    config = configparser.ConfigParser()
    config.read(f"{ROOT_DIR}/personal.ini")

    # Parse personal section
    personal_data = dict(config["personal"].items())

    projects = {
        section: dict(config[section].items())
        for section in config.sections()
        if section.startswith("project")
    }
    return {**personal_data, "projects": projects}


@app.route("/")
def homepage():
    data = parse_config()
    return render_template("homepage.html", **data)


if __name__ == "__main__":
    app.run(debug=True)
