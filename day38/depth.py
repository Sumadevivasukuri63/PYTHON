# Step 2: Define a function to check if the tree is balanced
class Solution:
    def isBalanced(self, root):
        # Helper function that returns the height if balanced, or -1 if not balanced
        def check(node):
            if node is None:
                return 0  # Base case: empty subtree has height 0

            left_height = check(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced

            right_height = check(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced

            if abs(left_height - right_height) > 1:
                return -1  # This node is unbalanced

            return 1 + max(left_height, right_height)

        return check(root) != -1  # ✅ This line is essential
sol = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Is the tree balanced?", sol.isBalanced(root))








# Step 1: Define a basic TreeNode class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Step 2: Define a function to check if the tree is balanced
class Solution:
    def isBalanced(self, root):
        # Helper function that returns the height if balanced, or -1 if not balanced
        def check(node):
            if node is None:
                return 0  # Empty trees have height 0 and are balanced

            left_height = check(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced

            right_height = check(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced

            # If difference is too big, return -1 (unbalanced)
            if abs(left_height - right_height) > 1:
                return -1

            # Return current height if balanced
            return 1 + max(left_height, right_height)

        # Start checking from the root
        return check(root) != -1