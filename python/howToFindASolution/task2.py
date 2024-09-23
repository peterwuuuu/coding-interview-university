# A group of people stands before you arranged in rows and columns. Looking from above, they form an R by C 
# rectangle of people. Your job is to return 2 specific heights – the first is computed by finding the shortest person 
# in each row, and then finding the tallest person among them (the “tallest-of-the-shortest”); 
# and the second is computed by finding the tallest person in each column, and then finding the shortest person 
# among them (the “shortest-of-the-tallest”).

def Task2(heights):
    row_len = len(heights)
    col_len = len(heights[0])
    shortest_heights = []
    highest_heights = []

    # 高效写法
    shortest_heights = [min(row) for row in heights]
    
    # 我的写法
    # for row in range(row_len):
    #     min_rows = min(heights[row])
    #     shortest_heights.append(min_rows) 
    
    for col in range(col_len):
        max_cols = max(row[col] for row in heights)
        highest_heights.append(max_cols)
    
    max_shortest = max(shortest_heights)
    min_highest = min(highest_heights)        
    
    return max_shortest, min_highest

heights = [
    [179, 170, 180],
    [165, 178, 185],
    [175, 181, 187]
]

result = Task2(heights)
print( result)