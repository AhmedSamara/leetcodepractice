class Solution:

    def recursiveRemoval(self, degrees, graph, zero_degree, all_zero, numCourses):
        # if nothing left to process, there is a cycle
        if not zero_degree:
            return []
        # root conidition for true: Graph is empty. Have removed all nodes.
        if len(all_zero) == numCourses:
            return all_zero

        next_zero = []
        # in graph, decrement the degree of all of its neighbors.
        for z in zero_degree:
            for dec in graph[z]:
                degrees[dec] -= 1
                if degrees[dec] == 0:
                    next_zero.append(dec)
        all_zero.extend(next_zero)
        return self.recursiveRemoval(degrees, graph, next_zero, all_zero, numCourses)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # tells you if course still has dependencies
        in_degree = [0] * numCourses
        # tells you which one to decrement when it's removed.
        graph = [[] for _ in range(numCourses)]
        # to take a, must first take b.
        for a, b in prerequisites:
            in_degree[a] += 1
            graph[b].append(a)
        init_zero = [i for i, d in enumerate(in_degree) if d == 0]
        return self.recursiveRemoval(in_degree, graph, init_zero, init_zero, numCourses)
