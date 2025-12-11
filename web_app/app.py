# from flask import Flask, render_template, request
# from story_engine.engine import StoryEngine

# app = Flask(__name__)
# engine = StoryEngine()

# @app.route("/", methods=["GET", "POST"])
# def home():
#     story = None
#     if request.method == "POST":
#         p = request.form["protagonist"]
#         ally = request.form["ally"]
#         ant = request.form["antagonist"]
#         setting = request.form["setting"]
#         conflict = request.form["conflict"]
#         obj = request.form["object"]
#         theme = request.form["theme"]
#         ending = request.form["ending"]
#         story = engine.generate(p, ally, ant, setting, conflict, obj, theme, ending)
#     return render_template("index.html", story=story)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
import sys
from pathlib import Path

# Ensure project root is on sys.path so sibling packages (like `story_engine`) can be
# imported when running this script directly (e.g. `python web_app/app.py`).
project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from story_engine.engine import StoryEngine

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    story = None
    info = None
    if request.method == "POST":
        p = request.form.get("protagonist", "").strip()
        ally = request.form.get("ally", "").strip() or "a companion"
        ant = request.form.get("antagonist", "").strip() or "an opposing force"
        setting = request.form.get("setting", "").strip()
        conflict = request.form.get("conflict", "").strip()
        obj = request.form.get("object", "").strip()
        theme = request.form.get("theme", "").strip() or "life"
        ending = request.form.get("ending", "hopeful").strip().lower()
        expand = True if request.form.get("expand") == "on" else False
        model = request.form.get("model", "").strip() or None

        engine = StoryEngine(model_name=model, do_expand=expand)
        story = engine.generate(p, ally, ant, setting, conflict, obj, theme, ending)
        info = {
            "model_used": model if expand and model else ("template-only" if not expand else "default-model")
        }

    return render_template("index.html", story=story, info=info)

if __name__ == "__main__":
    app.run(debug=True)
