planets = [0, 1, 2, 3]
coordinates = []

minForce = 1 / abs(planets[-1] - (planets[0] + 0.0001))
maxForce = 1 / abs(planets[0] - (planets[0] + 0.0001))

for i in range(len(planets) - 1):
    print(f"BETWEEN PLANETS: {i} and {i+1}")
    leftLimit = planets[i] + 0.00001
    rightLimit = planets[i + 1] - 0.00001

    negativeForce = 0

    while leftLimit + .00001 < rightLimit:

        mid = (leftLimit + rightLimit) / 2
        negativeForce = 0
        positiveForce = 0

        for k in range(i+1):
            # print(f"planets[k]: {planets[k]}, k: {k}")
            # print(f"negative mid: {mid}")
            negativeForce += abs(1 / (planets[k] - mid))

        for j in range(i + 1, len(planets)):
            # print(f"positive mid: {mid}")
            positiveForce += abs(1 / (planets[j] - mid))

        if negativeForce > positiveForce:
            leftLimit = mid
        else:
            rightLimit = mid

        if negativeForce > 0:
            pass
            '''
            print(f"left limit: {leftLimit}")
            print(f"asteroid position: {mid}")
            print(f"right limit: {rightLimit}")
            print(f"negativeForce: {negativeForce}")
            print(f"positiveForce: {positiveForce}")
            '''

    coordinates.append(leftLimit)

print(coordinates)

