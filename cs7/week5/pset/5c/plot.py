import matplotlib.pyplot as plt

x = [
2000,
4000,
8000,
16000,
32000,
]

y = [
0.1133,
0.4668,
1.8610,
7.6417,
30.2482,
]

a = [
400000,
800000,
1600000,
3200000,
6400000,
]

b = [
0.0275,
0.0544,
0.1182,
0.2154,
0.4524,
]

plt.plot(x, y)
plt.xscale("linear")
plt.yscale("linear")
plt.show()


