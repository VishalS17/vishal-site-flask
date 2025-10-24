
from flask import Flask, render_template, send_from_directory, abort, request, redirect, url_for, flash
import os
from vishal_site_assignment7 import DAL


app = Flask(__name__, template_folder="templates")
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret")

@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('css', filename)

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory('js', filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects', methods=['GET'])
def projects():
    rows = DAL.list_projects()
    return render_template('projects.html', projects=rows)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        imagefilename = request.form.get('imagefilename', '').strip()
        if not title or not description or not imagefilename:
            flash("All fields are required: Title, Description, and Image File Name.")
            return redirect(url_for('form'))
        # Do not handle file uploads here; just store the filename as instructed.
        try:
            DAL.insert_project(title, description, imagefilename)
            flash("Project added successfully!")
            return redirect(url_for('projects'))
        except Exception as e:
            flash(f"Error adding project: {e}")
            return redirect(url_for('form'))
    return render_template('form.html')

@app.route('/<page>')
def render_page(page):
    template_name = f"{page}.html"
    try:
        return render_template(template_name)
    except Exception:
        abort(404)

if __name__ == "__main__":
    # Ensure DB exists
    DAL.init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
