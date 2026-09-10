class Solution:

    def recursiveRemoval(self, degrees, graph, zero_degree, removed_count, numCourses):
        # root conidition for true: Graph is empty. Have removed all nodes.
        if removed_count == numCourses:
            return True
        # if nothing left to process, there is a cycle
        if not zero_degree:
            return False

        next_zero = []
        # in graph, decrement the degree of all of its neighbors.
        for z in zero_degree:
            for dec in graph[z]:
                degrees[dec] -= 1
                if degrees[dec] == 0:
                    next_zero.append(dec)
        return self.recursiveRemoval(degrees, graph, next_zero, removed_count + len(zero_degree), numCourses)

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # tells you if course still has dependencies
        in_degree = [0] * numCourses
        # tells you which one to decrement when it's removed.
        graph = [[] for _ in range(numCourses)]
        # to take a, must first take b.
        for a, b in prerequisites:
            in_degree[a] += 1
            graph[b].append(a)
        init_zero = [i for i, d in enumerate(in_degree) if d == 0]
        return self.recursiveRemoval(in_degree, graph, init_zero, 0, numCourses)
