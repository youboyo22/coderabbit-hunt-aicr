from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route("/api/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cur.execute(query)
    row = cur.fetchone()
    return {"user": row}
