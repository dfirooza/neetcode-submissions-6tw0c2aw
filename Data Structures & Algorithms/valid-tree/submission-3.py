class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #a valid tree has n-1 edges, and no cycles 
        #solution: we need to find a way to ensure there are no cycles
        #if there is a set of at least three nodes where every node has a connection to each other that is a cycle
        #Must just make sure that from any node you can reach all other nodes 

        if len(edges) != n-1: 
            return False


        neighbors = [[] for i in range(n)]
        for first, second in edges: 
            neighbors[first].append(second)
            neighbors[second].append(first)
        
        #now we have a mapping from each node to all its neighbors
        
        nodes = {0}
        q = [0]

        while q:
            curr = q.pop()
            for neighbor in neighbors[curr]: 
                if neighbor not in nodes: 
                    nodes.add(neighbor)
                    q.append(neighbor)
        
        return len(nodes) == n


        
        