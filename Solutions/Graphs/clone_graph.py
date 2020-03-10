
# Definition for a Node.


class Node(object):
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if node is None:
            return

        v = node.val

        connections = dict()

        q = [node]

        while len(q) > 0:
            n = q.pop()
            if n.val in connections:
                pass
            else:
                connections[n.val] = []
                for child in n.neighbors:
                    q.append(child)
                    connections[n.val].append(child.val)

        graph = dict()

        for key in connections:
            if key not in graph:
                graph[key] = Node(val=key)
            l = connections[key]
            for item in l:
                if item not in graph:
                    graph[item] = Node(val=item)

                graph[key].neighbors.append(graph[item])

        return graph[v]
