import random

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0,len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i-1]][solution[i]]
    return routeLength

def getNeighbors(solution):
    neighbors = []

    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)
    return neighbors

def getBestNeighbor(tsp, neighbors):
    bestRouteLength = routeLength(tsp, neighbors[0])
    bestNeighbor = neighbors[0]
    for neighbor in neighbors:
        currentRouteLength = routeLength(tsp, neighbor)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbor = neighbor
    return bestNeighbor, bestRouteLength


def genetic_algorith(tsp):
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp,currentSolution)
    neighbors = getNeighbors(currentSolution)
    bestNeighbor, bestNeighborRouteLength = getBestNeighbor(tsp, neighbors)

    while bestNeighborRouteLength < currentRouteLength:
        currentSolution = bestNeighbor
        currentRouteLength = bestNeighborRouteLength
        neighbors = getNeighbors(currentSolution)
        bestNeighbor, bestNeighborRouteLength = getBestNeighbor(tsp, neighbors)

    return currentSolution, currentRouteLength


    print(currentSolution)
    print(currentRouteLength)
    print(neighbors)

def main():
    tsp = [[0,11,10,9,15],
        [11,0,3,12,18],
        [10,3,0,11,17],
        [9,12,11,0,8],
        [15,18,17,8,0]
        ]

    print(genetic_algorith(tsp))

if __name__ == "__main__":
    main()
