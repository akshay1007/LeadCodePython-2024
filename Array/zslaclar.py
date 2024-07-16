##Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
## (i.e., from left to right, then right to left for the next level and alternate between).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Approch : 
# 1 . varialbe to store the zigzag  : Space : [] N element = O(N)
# 2. take a dequeue --> hold the binary tree  O(N)
# 3. BFS :  
#     if dequeue is empty : at root  / O(1)
#         indicator -> left_to_right 
#                   -> right_to_left
#         current_stage 
# 4. Print the result 


from collections import deque
class Solution:
    def zigzag(self,root):
        if not root : 
            return []
        result = []
        queue = deque([root])
        current_state = []

        while queue: 
            check the state 

            for _ in range()
            if lef_to_right : 






if __name__ == "__main__":
    Input = [3,9,20,null,null,15,7]
    obj = Solution()
    obj.zigzag(Input)
