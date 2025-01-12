import json
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


with open('steam.json', 'r') as json_file:
    data = json.load(json_file)


with open('steam.json', 'r') as json_file:
    game_data = json.load(json_file)


spelers = [int(data["owners"].split(" - ")[1].replace(",", "")) for data in game_data]
likes = [data["positive_ratings"] for data in game_data]

X = np.array(spelers).reshape(-1, 1)
y = np.array(likes).reshape(-1, 1)


X_b = np.c_[np.ones((len(X), 1)), X]

def gradient_afdalingen(X, y, leer_snelheid=1e-15, iteraties=1000):
    m = len(X)
    np.random.seed(42)
    theta = np.random.randn(X.shape[1])

    for iteratie in range(iteraties):
        gradiënten = 2 / m * X.T.dot(X.dot(theta) - y.ravel())
        theta -= leer_snelheid * gradiënten
    return theta

theta_opt = gradient_afdalingen(X_b, y)

beta_0, beta_1 = theta_opt

positive_ratings = [item["positive_ratings"] for item in data]
negative_ratings = [item["negative_ratings"] for item in data]

x = np.array(positive_ratings)
y = np.array(negative_ratings)

a, b = np.polyfit(x, y, 1)  # a is de helling, b is het intercept

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='purple', alpha=0.6, label='Data')

plt.plot(x, a * x + b, color='red', label=f'Lijn: y = {a:.2f}x + {b:.2f}')

plt.xlabel("Positieve Beoordelingen")
plt.ylabel("Negatieve Beoordelingen")
plt.title("Positieve vs. Negatieve Beoordelingen met Regressielijn")
plt.legend()
plt.grid(True)
plt.show()

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

    print(f"Er zijn op Steam {aantal_games} games beschikbaar.")
    print(f"Het gemiddelde van de gemiddelde speeltijd per game is {gemiddelde_speeltijd_afgerond:5} minuten.")
    print(f"The median of the median playing times is {mediaan} minutes.")