# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/24 17:51
# @Software: PyCharm
from collections import deque

# 0 means road, and 1 means wall
maze = [
    [0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0]
]


def dfs_maze_path(maze):
    m, n = len(maze), len(maze[0])
    stack = []
    stack.append((0, 0))
    while stack:
        x, y = stack[-1]
        if x == m - 1 and y == n - 1:
            for p in stack:
                if p == stack[-1]:
                    print(p)
                else:
                    print(p, end="->")
            break
            # return

        for nx, ny in zip((x + 1, x - 1, x, x), (y, y, y + 1, y - 1)):
            if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                stack.append((nx, ny))
                maze[nx][ny] = 2
                break
        else:
            maze[nx][ny] = 2
            stack.pop()
    else:
        print("no path in the maze.")


def bfs_maze_path(maze):
    def print_path(path):
        cur = path[-1]
        real_path = []
        real_path.append(cur[0:2])
        while cur[2] != -1:
            cur = path[cur[2]]
            real_path.append(cur[0:2])
        for p in real_path[::-1]:
            print(p) if p == real_path[0] else print(p, end="->")

    m, n = len(maze), len(maze[0])
    start = (0, 0, -1)
    queue = deque()
    queue.append(start)
    path = []
    while queue:
        cur = queue.popleft()
        path.append(cur)
        x, y = cur[0], cur[1]
        if x == m - 1 and y == n - 1:
            print_path(path)
            break
            # return
        for nx, ny in zip((x + 1, x - 1, x, x), (y, y, y + 1, y - 1)):
            if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                maze[nx][ny] = 2
                queue.append((nx, ny, len(path) - 1))
    else:
        print("no path in the maze.")


if __name__ == '__main__':
    import copy

    _maze = copy.deepcopy(maze)
    print("---dfs---")
    dfs_maze_path(maze)
    print("---bfs---")
    bfs_maze_path(_maze)


