from flask import Flask, render_template
from helpers.definitions import ROOT_DIR
import configparser

app = Flask(__name__)

def parse_config():
    config = configparser.ConfigParser()
    config.read(f"{ROOT_DIR}/personal.ini")
    name = config.get("personal", "name")
    location = config.get("personal", "location")
    # picture = config.get("personal", "picture")
    linkedin = config.get("personal", "linkedin")
    github = config.get("personal", "github")
    resume = config.get("personal", "resume")
    blog = config.get("personal", "blog")
    return name, location, linkedin, github, resume, blog

@app.route('/')
def homepage():
    name, location, linkedin, github, resume, blog = parse_config()
    return render_template('homepage.html', name=name, location=location, linkedin=linkedin, github=github, resume=resume, blog = blog)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5001, debug=True)
    app.run(debug=True)
