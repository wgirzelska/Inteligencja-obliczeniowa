import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

miasta = pd.read_csv('miasta.csv')
# a)
print(miasta)
print(miasta.values)

# b)
nowy_wiersz = {"Rok": [2010], "Gdansk": [460], "Poznan": [555], "Szczecin": [405]}

df = pd.DataFrame(nowy_wiersz)

df.to_csv('miasta.csv', mode='a', index=False, header=False)
miasta2 = pd.read_csv('miasta.csv')

print(miasta2)

# c)

onlyGdansk = pd.read_csv("miasta.csv", usecols = ['Gdansk'])
rok = pd.read_csv("miasta.csv", usecols = ['Rok'])

ypoints = np.array(onlyGdansk)
xpoints = np.array(rok)

plt.scatter(xpoints, ypoints, color='red')
plt.plot(xpoints, ypoints, color='red')
plt.xlabel('Rok')
plt.ylabel('Ludność')
plt.title('Ludność Gdańska')
plt.show()

# d)

onlyPoznan = pd.read_csv("miasta.csv", usecols = ['Poznan'])
onlySzczecin = pd.read_csv("miasta.csv", usecols = ['Szczecin'])

plt.plot(xpoints, onlyGdansk, label='Gdansk')
plt.plot(xpoints, onlyPoznan, label='Poznan')
plt.plot(xpoints, onlySzczecin, label='Szczecin')

plt.xlabel('Rok')
plt.ylabel('Ludność wszystkich miast')
plt.ylabel('Ludność')
plt.legend()
plt.show()

# e)

miasta_std = (miasta - miasta.mean()) / miasta.std()

print("Średnia po skalowaniu:", miasta_std.mean())
print("Odchylenie standardowe po skalowaniu:", miasta_std.std())

# f)

miasta_norm = (miasta - miasta.min()) / (miasta.max() - miasta.min())

print("Wartość minimalna po skalowaniu:", miasta_norm.min())
print("Wartość maksymalna po skalowaniu:", miasta_norm.max())

