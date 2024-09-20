# N tasks are written down in the form of a circular list, so the first task is adjacent to the last one. A number n is also given. 
# Starting with the first task, move clockwise (from element 1 in the list to element 2 in the list and so on), counting from 1 to n. 
# When your count reaches n, remove that task from the list and start counting from the next available task. 
# Repeat this procedure until one task remains. Return it.


def Task1(nums, n):
    index = 0
    while (len(nums) != 1):
        index = (index + n - 1) % len(nums) # 每次的index对nums的长度取模，如果index比len(nums)小，就直接从当前index开始
                                            # 但是如果index比len(nums)大，取模之后的结果就相当于nums首尾相连之后超出的部分继续从nums开头开始
        nums.pop(index)
    return nums[0]

nums = [1,2,3,4,5]
n = 3

result = Task1(nums, n)        

print(result)
    