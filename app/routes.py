from flask import render_template, request, redirect, abort
from app import app, db
from app.models import Link
import random, string

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form.get("url")
        code = generate_code()
        new_link = Link(url=original_url, code=code)
        db.session.add(new_link)
        db.session.commit()
        return render_template("index.html", short_url=request.host_url + code)
    return render_template("index.html")

@app.route("/<code>")
def redirect_link(code):
    link = Link.query.filter_by(code=code).first()
    if link:
        link.clicks += 1
        db.session.commit()
        return redirect(link.url)
    else:
        abort(404)

@app.route("/stats/<code>")
def stats(code):
    link = Link.query.filter_by(code=code).first()
    if not link:
        abort(404)
    return f"URL: {link.url} | Clicks: {link.clicks}"
