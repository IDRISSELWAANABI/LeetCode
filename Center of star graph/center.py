class Solution:
def findCenter(self, edges: List[List[int]]) -> int:
    degree = collections.Counter()
    for node1, node2 in edges:
        degree[node1] += 1
        degree[node2] += 1

    for node, count in degree.items():
        if count == len(edges):
            return node