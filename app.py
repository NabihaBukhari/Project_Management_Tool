from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db_connection, init_db

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Initialize database
init_db()

# --- HOME ---
@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    projects = conn.execute('SELECT * FROM projects WHERE created_by = ?', (session['user_id'],)).fetchall()
    conn.close()
    return render_template('home.html', projects=projects, user=session['name'])

# --- SIGNUP ---
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', 
                         (name, email, password))
            conn.commit()
            flash('Account created! Please log in.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email already exists!')
        finally:
            conn.close()

    return render_template('signup.html')

# --- LOGIN ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['name'] = user['name']
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials!')
    return render_template('login.html')

# --- LOGOUT ---
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# --- PROJECTS ---
@app.route('/projects', methods=['GET', 'POST'])
def projects():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['description']
        conn.execute('INSERT INTO projects (name, description, created_by) VALUES (?, ?, ?)',
                     (name, desc, session['user_id']))
        conn.commit()

    projects = conn.execute('SELECT * FROM projects WHERE created_by = ?', 
                            (session['user_id'],)).fetchall()
    conn.close()
    return render_template('projects.html', projects=projects)

# --- TASKS ---
@app.route('/tasks/<int:project_id>', methods=['GET', 'POST'])
def tasks(project_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    if request.method == 'POST':
        title = request.form['title']
        conn.execute('INSERT INTO tasks (project_id, title) VALUES (?, ?)', (project_id, title))
        conn.commit()
    tasks = conn.execute('SELECT * FROM tasks WHERE project_id = ?', (project_id,)).fetchall()
    conn.close()
    return render_template('tasks.html', tasks=tasks, project_id=project_id)

# --- UPDATE TASK STATUS ---
@app.route('/update_task/<int:task_id>/<status>')
def update_task(task_id, status):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
    conn.commit()
    conn.close()
    return redirect(request.referrer)

if __name__ == '__main__':
    app.run(debug=True)
