from flask import Flask, render_template, redirect, url_for, request, session, flash
import json
import subprocess

app = Flask(__name__)
app.secret_key = "********"
@app.route('/')
def home():
    with open("steam.json", "r") as f:
        games = json.load(f)
    return render_template('home.html', games=games)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for("user", usr=user))
    else:
        if 'user' in session:
            flash('You are already logged in!')
            return redirect(url_for('user'))
        return render_template("login.html")
@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        flash(f"Je bent nu ingelogd {user}")
        return render_template("user.html", user=user)
    else:
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    if 'user' in session:
        user = session['user']
        flash(f'You have been logged out. {user}')
    session.pop('user', None)

    return redirect(url_for("login"))

@app.route('/statistic')
def statistic():
    with open("steam.json", "r") as f:
        data = json.load(f)

    totaal_gespeeld = sum(spel['average_playtime'] for spel in data)
    aantal_games = len(data)
    gemiddelde_speeltijd = totaal_gespeeld / aantal_games
    gemiddelde_speeltijd_afgerond = round(gemiddelde_speeltijd, 2)
    gesorteerd_mediaan = sorted(spel['average_playtime'] for spel in data)

    n = len(gesorteerd_mediaan)
    if n % 2 == 1:
        mediaan = gesorteerd_mediaan[n // 2]
    else:
        mediaan = (gesorteerd_mediaan[n // 2 - 1] + gesorteerd_mediaan[n // 2]) / 2


    flash(f"There are {aantal_games} games available on Steam.")
    flash(f"The average of the average playing time per game is {gemiddelde_speeltijd_afgerond} minutes.")
    flash(f"The median of the median playing times is {mediaan} minutes.")


    return render_template("statistic.html")

@app.route('/timer')
def timer():
    # Voer timer.py uit
    subprocess.Popen(["python", "timer.py"])
    return render_template("timer.html")

@app.route("/<bestaatniet>/")
def bestaatniet(bestaatniet):
    return f"De pagina {bestaatniet} bestaat niet."

if __name__ == '__main__':
    app.run(debug=True)