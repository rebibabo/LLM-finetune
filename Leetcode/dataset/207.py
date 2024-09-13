class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge, indegree = self.construct(prerequisites)
        while True:
            f = self.find(indegree)
            if f == -1:
                break
            if f in edge:
                for next in edge[f]:
                    indegree[next] -= 1
            del indegree[f]
        return not indegree

    def construct(sel, prerequisites):
        edge, indegree = {}, {}
        for a, b in prerequisites:
            edge.setdefault(a, set())
            edge[a].add(b)
            indegree.setdefault(a, 0)
            indegree.setdefault(b, 0)
            indegree[b] += 1
        return edge, indegree

    def find(self, indegree):
        for i, ind in indegree.items():
            if ind == 0:
                return i
        return -1