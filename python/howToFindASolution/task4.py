import heapq

class WalkingHome:
    def fewestCrossings(self, map):
        rows = len(map)
        cols = len(map[0])
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Find positions of S and H
        start = end = None
        for r in range(rows):
            for c in range(cols):
                if map[r][c] == 'S':
                    start = (r, c)
                elif map[r][c] == 'H':
                    end = (r, c)
        
        # Priority queue for (crossings, row, col)
        pq = [(0, start[0], start[1])]  # (crossings, row, col)
        visited = set()
        visited.add((start[0], start[1]))
        
        while pq:
            crossings, r, c = heapq.heappop(pq)
            
            # If we reach home
            if (r, c) == end:
                return crossings
            
            # Check all four directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                crossing_this_move = False
                
                while 0 <= nr < rows and 0 <= nc < cols and map[nr][nc] not in '*F':
                    if map[nr][nc] in '|-':  # It's a road
                        if not crossing_this_move:
                            crossings += 1  # Count this crossing
                            crossing_this_move = True  # Only count the first crossing in this direction
                    else:
                        crossing_this_move = False  # Reset crossing flag on empty space
                    
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        heapq.heappush(pq, (crossings, nr, nc))
                    
                    nr += dr
                    nc += dc
        
        return -1  # If home is unreachable

# Example usage
walking_home = WalkingHome()
print(walking_home.fewestCrossings(["S.|..", 
                                    "..|.H"]))  # Output: 1
print(walking_home.fewestCrossings(["S.|..", 
                                    "..|.H", 
                                    "..|..", 
                                    "....."]))  # Output: 0
print(walking_home.fewestCrossings(["H|.|.|.|.|.|.|.|.|.|.|.|.|.", 
                                     "F|F|F|F|F|F|F|F|F|F|F|F|F|-",
                                     "S|.|.|.|.|.|.|.|.|.|.|.|.|."]))  # Output: 27
print(walking_home.fewestCrossings(["S.F..",
                                    "..F..",
                                    "--*--",
                                    "..|..",
                                    "..|.H"])) # Output: 2
print(walking_home.fewestCrossings(["S.||...",
                                    "..||...",
                                    "..||...",
                                    "..||..H"])) # Output: 1


# # Create an empty heap
# min_heap = []

# # Adding elements
# heapq.heappush(min_heap, 5)
# heapq.heappush(min_heap, 3)
# heapq.heappush(min_heap, 8)
# heapq.heappush(min_heap, 1)

# print("Heap after additions:", min_heap)  # Output may not be sorted

# # Pop the smallest element
# smallest = heapq.heappop(min_heap)
# print("Smallest element popped:", smallest)  # Output: 1
# print("Heap after popping the smallest element:", min_heap)

# # Peek at the smallest element
# next_smallest = min_heap[0]
# print("Next smallest element:", next_smallest)  # Output: 3

# # Adding more elements
# heapq.heappush(min_heap, 2)
# heapq.heappush(min_heap, 6)

# print("Heap after more additions:", min_heap)  # Output may not be sorted

# # Pop all elements to show the order
# sorted_elements = []
# while min_heap:
#     sorted_elements.append(heapq.heappop(min_heap))

# print("Elements in sorted order:", sorted_elements)  # Output: [2, 3, 5, 6, 8]