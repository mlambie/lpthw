pi = 0.0
modifier = -1

# Produces pi to 5 sig fig
cycles = 500000

for x in range(1, cycles * 2, 2):
	modifier = modifier * -1
	pi = pi + (modifier * 4.0 / x)
	print(pi)
