import os
from flask import Flask, render_template, render_template_string, request
from jinja2.exceptions import TemplateSyntaxError


app = Flask(__name__)


@app.route("/")
def index():

    exploit = request.args.get('exploit')
    rendered_template = render_template("app.html", exploit=exploit)

    try:
        render_template_string(rendered_template)
    except TemplateSyntaxError:
        rendered_template = render_template("app.html", exploit='Not a valid Jinja2 expression.')
    finally:
        return render_template_string(rendered_template)

if __name__ == "__main__":
    app.run(debug=True)