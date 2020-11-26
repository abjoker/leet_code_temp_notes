class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = []
        
        if not root:
            return []
        else:
            q.append(root)
            
        
        # while q is not empty
        while q:
            # cache size: size of the children [0, 1, or 2]
            cur, cache_size = [], len(q)
            for _ in range(cache_size):
                node = q.pop(0)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                

                cur.append(node.val)
                
            res.append(cur)
            
        return res
