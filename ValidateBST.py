class tree():
    def __init__(self , val , left = None , right = None ):
        self.val, self.right , self.left = val , right , left

def validate(root) :
    if not root:
        return True
    if root.left :
        root.left < root
    if root.right:
        root.right > root
    root.left =	validate(root.left)
    root = validate(root)
    root.right = validate(root.right)
