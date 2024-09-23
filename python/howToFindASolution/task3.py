# A word composed of four Latin lowercase letters is given. With a single button click you can change any letter to the previous or next letter 
# in alphabetical order (for example ‘c’ can be changed to ‘b’ or ‘d’). The alphabet is circular, thus ‘a’ can become ‘z’, and ‘z’ can become ‘a’ with one click.

# A collection of constraints is also given, each defining a set of forbidden words. A constraint is composed of 4 strings of letters. 
# A word is forbidden if each of its characters is contained in corresponding string of a single constraint, i.e. first letter is contained in the first string, 
# the second letter – in the second string, and so on. For example, the constraint “lf a tc e” defines the words “late”, “fate”, “lace” and “face”.

# You should find the minimum number of button presses required to reach the word finish from the word start without passing through forbidden words, 
# or return -1 if this is not possible.

from collections import deque


# def generate_forbidden_words(constraints):
#     forbidden = set()
#     for i in constraints[0]:
#         for j in constraints[1]:
#             for k in constraints[2]:
#                 for l in constraints[3]:
#                     forbidden.add(i + j + k + l)
#     return forbidden

# def get_neighbors(word):
#     neighbor = []
#     for i in range(len(word)):
#         for change in [-1, 1]:
#             new_letter = chr((ord(word[i]) - ord('a') + change) % 26 + ord('a'))
#             new_word = word[:i] + new_letter + word[i+1:]
#             neighbor.append(new_word)
#     return neighbor

# def Task3(start, finish, constraints):
#     forbidden_words = generate_forbidden_words(constraints)
    
#     if start in forbidden_words or finish in forbidden_words:
#         return -1
    
#     queue = deque([(start, 0)])
#     visited = set()
#     visited.add(start)
    
#     while queue:
#         current_word, steps = queue.popleft()
        
#         if current_word == finish:
#             return steps
        
#         for neighbor in get_neighbors(current_word):
#             if neighbor not in forbidden_words and neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append((neighbor, steps + 1)) 
        
#     return -1 

# start = ('bscd')
# finish = ('abcd')
# constraints = ['ws', 'ea', 'za', 'gh']
# result = Task3(start, finish, constraints)
# print(result)



def generate_constraints(constraints):
    forbiddens = set()
    for i in constraints[0]:
        for j in constraints[1]:
            for k in constraints[2]:
                for l in constraints[3]:
                    forbiddens.add(i+j+k+l)
    return forbiddens

def get_neighbors(current_word):
    neighbor = []
    
    for i in range(len(current_word)):
        for change in [-1, 1]:
            new_letter = chr((ord(current_word[i]) - ord('a') + change) % 26 + ord('a'))
            new_word = current_word[:i] + new_letter + current_word[i+1:]
            neighbor.append(new_word)
    return neighbor

def Task3(start, finish, constraints):
    forbiddens = generate_constraints(constraints)
    
    if start in forbiddens or finish in forbiddens:
        return -1
    
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        current_word, steps = queue.popleft()
        
        if current_word == finish:
            return steps
        
        for neighbor in get_neighbors(current_word):
            if neighbor not in forbiddens and neighbor not in visited:
                queue.append((neighbor, steps + 1))
                visited.add(neighbor)
    return -1

start = 'bscd'
finish = 'abcd'
constraints = ['ws', 'ea', 'za', 'gh']
result = Task3(start, finish, constraints)
print(result)