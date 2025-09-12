from flask import Flask, render_template
from models import db, SpendingModel
from flask_migrate import Migrate
from sqlalchemy import text
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return render_template("index.html")

@app.get("/testdb")
def db_ok():
    db.session.execute(text("SELECT 1"))
    return "DB OK ✅"

@app.get("/spending/all")
def spending_all():
    rows = SpendingModel.query.order_by(SpendingModel.id.desc()).all()
    return "<br>".join([f"{r.id} — {r.item} — {r.cost} — {r.time}" for r in rows]) or "No rows yet."

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)