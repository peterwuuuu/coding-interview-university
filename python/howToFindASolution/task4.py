from collections import deque

class WalkingHome:
    def fewestCrossings(self, map):
        rows, cols = len(map), len(map[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        # Find the start (S) and home (H) positions
        start, home = None, None
        for i in range(rows):
            for j in range(cols):
                if map[i][j] == 'S':
                    start = (i, j)
                if map[i][j] == 'H':
                    home = (i, j)
        
        # BFS initialization
        queue = deque([(start[0], start[1], 0)])  # (row, col, crossings)
        visited = set([(start[0], start[1])])  # Store (row, col) only
        
        while queue:
            r, c, crossings = queue.popleft()
            
            # Debugging: Print current position and crossing count
            print(f"Current position: ({r}, {c}), Crossings: {crossings}")
            
            # If we've reached the home, return the number of crossings
            if (r, c) == home:
                print(f"Reached home with {crossings} crossings.")
                return crossings
            
            # Explore the four directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Cannot move into fences or intersections
                    if map[nr][nc] == 'F' or map[nr][nc] == '*':
                        continue
                    
                    # If moving into an empty space or the home
                    if map[nr][nc] == '.' or map[nr][nc] == 'H':
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc, crossings))
                            print(f"Move to empty space or home at: ({nr}, {nc}), Crossings: {crossings}")
                    
                    # If we are crossing a vertical road ('|')
                    elif map[nr][nc] == '|' and dr != 0:  # Must move horizontally across vertical road
                        # Traverse vertically to handle multi-lane road as a single crossing
                        while nr >= 0 and nr < rows and map[nr][nc] == '|':
                            nr += dr
                        nr -= dr  # Adjust to last valid position
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc, crossings + 1))
                            print(f"Crossed vertical road to: ({nr}, {nc}), Crossings: {crossings + 1}")
                    
                    # If we are crossing a horizontal road ('-')
                    elif map[nr][nc] == '-' and dc != 0:  # Must move vertically across horizontal road
                        # Traverse horizontally to handle multi-lane road as a single crossing
                        while nc >= 0 and nc < cols and map[r][nc] == '-':
                            nc += dc
                        nc -= dc  # Adjust to last valid position
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc, crossings + 1))
                            print(f"Crossed horizontal road to: ({nr}, {nc}), Crossings: {crossings + 1}")
        
        # If the loop ends and we didn't reach home, return -1
        print("No valid path to home.")
        return -1

# Example usage:
map1 = ["S.|..", "..|.H"]
solver = WalkingHome()
print(solver.fewestCrossings(map1))  # Should output: 1
