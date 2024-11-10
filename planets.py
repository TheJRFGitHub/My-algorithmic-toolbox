planets = [0, 1, 2, 3]
coordinates = []

minForce = 1 / abs(planets[-1] - (planets[0] + 0.0001))
maxForce = 1 / abs(planets[0] - (planets[0] + 0.0001))

negativeForce = 0

for i in range(len(planets) - 1):

    positiveForce = 0
    leftLimit = planets[i] + 0.001
    rightLimit = planets[i + 1] - 0.001
    print(f"left limit: {leftLimit}")
    print(f"right limit: {rightLimit}")
    while leftLimit + .001 < rightLimit:

        mid = (leftLimit + rightLimit) / 2
        negativeForce += abs(1 / (i - mid))

        for j in range(i + 1, len(planets)):
            positiveForce += abs(1 / (j - mid))

        if negativeForce > positiveForce:
            leftLimit = mid
        else:
            rightLimit = mid
    print(f"coordinates: {mid}")
    print(f"negativeForce: {negativeForce}")
    print(f"positiveForce: {positiveForce}")

print(coordinates)
