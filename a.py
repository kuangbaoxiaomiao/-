import heapq
from collections import deque


class Node:
    def __init__(self, x, y, length, path):
        self.x = x
        self.y = y
        self.length = length
        self.path = path

    def __lt__(self, other):
        return self.length < other.length


def get_neighbors(x, y, n, m, board):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors


def a_star_search(n, m, board, start, end):
    # 初始化优先队列和已访问集合
    frontier = []
    visited = set()
    heapq.heappush(frontier, Node(start[0], start[1], 0, [(start[0], start[1])]))
    shortest_path = None
    shortest_length = float('inf')

    while frontier:
        current_node = heapq.heappop(frontier)
        if (current_node.x, current_node.y) == (end[0], end[1]):
            if current_node.length < shortest_length:
                shortest_length = current_node.length
                shortest_path = current_node.path
            continue

        if (current_node.x, current_node.y) in visited:
            continue

        visited.add((current_node.x, current_node.y))

        for neighbor in get_neighbors(current_node.x, current_node.y, n, m, board):
            new_length = current_node.length + 1
            new_path = current_node.path + [(neighbor[0], neighbor[1])]
            new_node = Node(neighbor[0], neighbor[1], new_length, new_path)
            heapq.heappush(frontier, new_node)

    return shortest_length, shortest_path


# 获取用户输入
n,m = map(int,input().split())
board = []
for i in range(n):
    row = list(map(int, input(f"请输入第{i + 1}行（用空格分隔0和1）：").split()))
    if len(row) != m:
        print("输入错误：每行的长度必须与列数m匹配。")
        exit()
    board.append(row)

start = tuple(map(int, input("请输入起点坐标（格式为x y，索引从1开始）：").split()))
start = (start[0] - 1, start[1] - 1)  # 转换为0索引

end = tuple(map(int, input("请输入终点坐标（格式为x y，索引从1开始）：").split()))
end = (end[0] - 1, end[1] - 1)  # 转换为0索引

# 调用搜索函数
length, path = a_star_search(n, m, board, start, end)
print(f"最短路径长度：{length}")
if path:
    print(f"最短路径（从1索引表示）：{[(p[0] + 1, p[1] + 1) for p in path]}")
else:
    print("没有找到路径。")