from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create database table
def init_db():
    conn = sqlite3.connect("exam.db")
    conn.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            score INTEGER
        )
    ''')
    conn.close()

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/quiz', methods=['POST'])
def quiz():
    name = request.form['name']
    return render_template("quiz.html", name=name)

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    score = 0

    if request.form.get('q1') == "b":
        score += 1
    if request.form.get('q2') == "b":
        score += 1
    if request.form.get('q3') == "b":
        score += 1

    conn = sqlite3.connect("exam.db")
    conn.execute("INSERT INTO results (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

    return render_template("result.html", name=name, score=score)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)