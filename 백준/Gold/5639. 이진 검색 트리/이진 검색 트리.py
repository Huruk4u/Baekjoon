import sys
from collections import defaultdict
sys.setrecursionlimit(1000000001)
input = sys.stdin.readline



def build_tree(nodes):
    root = nodes[0]
    child[root] = [None, None]
    if len(nodes) == 1:
        return
    else:
        left, right = [], []
        for i in range(1, len(nodes)):
            if root > nodes[i]:
                left.append(nodes[i])
            else:
                right.append(nodes[i])

        if left:
            child[root][0] = left[0]
            parent[left[0]] = root
            build_tree(left)
        if right:
            child[root][1] = right[0]
            parent[right[0]] = root
            build_tree(right)
    return


def lrd(node):
    if child[node][0] is not None: lrd(child[node][0])
    if child[node][1] is not None: lrd(child[node][1])
    print(node)
    return

if __name__ == '__main__':
    parent, child = defaultdict(int), defaultdict(list)
    nodes = []
    while True:
        try:
            ipt = int(input().strip())
            nodes.append(ipt)
        except:
            break

    root = nodes[0]
    build_tree(nodes)
    # print("parent", parent)
    # print("child", child)
    lrd(root)
    