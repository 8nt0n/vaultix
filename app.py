import os

# import dbHelpers

import cs50
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, Response, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
import requests




# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

print(__name__ == '__main__')


Username = "none"

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database (Change later)
db = SQL("sqlite:///streamed.db")


@app.route("/")
@login_required
def index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        
        #get username, password, confirmation
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        # error checking
        if username == "" or len(db.execute('SELECT username FROM users WHERE username = ?', username)) > 0:
            return apology("Invalid Username: Blank, or already exists")
        if password == "" or password != confirmation:
            return apology("Invalid Password: Blank, or does not match")
        
        # Add new user to users db (includes: username and HASH of password)
        db.execute('INSERT INTO users (username, hash) \
                VALUES(?, ?)', username, generate_password_hash(password))
        
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        
        # Log user in, i.e. Remember that this user has logged in
        session["user_id"] = rows[0]["id"]
        
        # Redirect user to home page
        return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        # Forget any user_id
        session.clear()

        # User reached route via POST (as by submitting a form via POST)
        if request.method == "POST":
            Username = request.form.get("username")
            print(Username)
            # Ensure username was submitted
            if not request.form.get("username"):
                return apology("must provide username", 403)

            # Ensure password was submitted
            elif not request.form.get("password"):
                return apology("must provide password", 403)

            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

            # Ensure username exists and password is correct
            if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
                return apology("invalid username and/or password", 403)

            # Remember which user has logged in
            session["user_id"] = rows[0]["id"]

            # Redirect user to home page
            return redirect("/")


@app.route("/logout")
@login_required
def logout():

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/profile")
@login_required
def profile():
    if request.method == "GET":
        return render_template("profile.html")




@app.route("/videos")
@login_required
def videos():
    if request.method == "GET":
        #tags = db.execute('FROM vTags SELECT *')
        #print(tags)

        # TODO: choose 5 random categories

        return(render_template("videos.html"))


@app.route('/AppIndex_script')
def AppIndex_script():
    try:
        # Fetch the script from an external URL
        script_url = "https://cdn.jsdelivr.net/gh/8nt0n/VaultixStore/INDEX/AppStoreIndex.js"
        external_response = requests.get(script_url)
        external_response.raise_for_status()  # Raise an error for bad status codes
        
        # Return the fetched content as a Flask response
        return Response(external_response.content, content_type="application/javascript")
    except requests.exceptions.RequestException as e:
        return Response(f"Error fetching script: {e}", status=500)


@app.route('/AppStoreAppInstall', methods=['POST'])
def AppStoreAppInstall():
    
    # Extract the AppId from the request
    data = request.json
    AppId = data.get('AppId')
    
    # Perform actions based on the AppId
    return jsonify({"message": f"App with ID {AppId} clicked!"})
