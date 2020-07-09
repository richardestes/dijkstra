# Dijkstra Algorithm

# Let distance of start vertex from start vertex = 0
# Let distance of all other vertices from start = ∞

# Repeat
#   Visit the unvisited vertex with the smallest known distance from start vertex
#   For the current vertex, examine its unvisited neighbors
#   For the current vertex, calculate the distance of each neighbor from start vertex
#   If the calculated distance of a vertex is less than the known distance:
#       Update the shortest distance
#   Update the previous vertex for each of the updated distances
#   Add the current vertex to the list of visited vertices
# Until all vertices visited

# WHILE vertices remain unvisited
#   Visit unvisited vertex with smallest known distance from start vertex (call this currentVertex)
#   FOR each unvisited neighbor of the current vertex
#       Calculate the distance from start vertex
#       IF the calculated distance of this vertex is less than the know distance:
#           UPDATE the shortest distance to this vertex
#           UPDATE the previous vertex with the current vertex
#       END IF
#   NEXT unvisited neighbor
#   Add the current vertex to the list of visited vertices
# END WHILE


import math

print(math.inf)
