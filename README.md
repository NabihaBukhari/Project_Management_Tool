
# Project Management Tool

A simple **Project Management Tool** built using **Python Flask** and **SQLite**, with HTML and CSS for frontend structure and styling. This project allows users to manage projects, tasks, and track progress efficiently.

---

## Project Brief

This tool enables users to log in and access their personalized dashboard. Features include:

- **User Authentication**: Users can sign up or log in to access the system.
- **Dashboard Overview**: Upon logging in, the user sees the total number of projects and a list of all projects.
- **Project Management**: Users can:
  - View tasks associated with a specific project
  - Add new tasks and track their status (similar to a to-do list)
  - Create new projects to manage their work

---

## How to Run the Project

1. **Clone the repository**
2. **install dependencies**
3. **Run Flask application** python app.py (in terminal)
This will start the server and open the website showing the login page.<br>
If you are a new user, create an account using the Sign Up page.<br>
For existing users, enter your login details to access the dashboard.

4. **View database activity**
Run the view_db.py file: 
python view_db.py (in terminal)
This will display database activity and help you monitor actions on the website.

API Endpoints Summary

This project uses Python Flask as a backend but does not expose public API endpoints. Version control is handled using Git, where changes are committed and tracked.
<hr>

Assumptions & Possible Improvements

This project was developed in a short timeframe, combining basic Python Flask knowledge with as many features as possible.

Current limitations and future improvements could include:

Adding full CRUD functionality for projects and tasks

Enhanced UI/UX for better user experience

Integrating user roles (admin, member) for better access control

Adding notifications or email reminders for tasks

Migrating from SQLite to a more robust database like MySQL or PostgreSQL

Implementing RESTful API endpoints for external integrations

<hr>

Technology Stack

Backend: Python Flask

Database: SQLite

Frontend: HTML, CSS

Version Control: Git

Contact

**Name: Nabiha Bukhari**

**Email: nabiha.bukhari@hotmail.com**