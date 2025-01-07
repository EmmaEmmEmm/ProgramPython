from collections import defaultdict, deque

def find_shortest_path(N, X, Z, rest_points, roads):
    # 建立鄰接表
    graph = defaultdict(list)
    for A, B in roads:
        graph[A].append(B)
        graph[B].append(A)

    # 初始化最短路徑
    shortest_path = None
    best_rest_point = None

    # BFS 搜索每個休息點的最短路徑
    for rest_point in rest_points:
        # 從 X 到休息點
        queue = deque([(X, [X])])
        visited = set()
        path_to_rest = None

        while queue:
            current, path = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            if current == rest_point:
                path_to_rest = path
                break

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        if not path_to_rest:
            continue

        # 從休息點到 Z
        queue = deque([(rest_point, [rest_point])])
        visited = set()
        path_to_z = None

        while queue:
            current, path = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            if current == Z:
                path_to_z = path
                break

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        if not path_to_z:
            continue

        # 合併路徑
        full_path = path_to_rest[:-1] + path_to_z

        # 更新最短路徑
        if not shortest_path or len(full_path) < len(shortest_path):
            shortest_path = full_path
            best_rest_point = rest_point

    # 輸出結果
    if shortest_path:
        print(best_rest_point)
        print(" ".join(map(str, shortest_path)))
    else:
        print("NO")

# 測試資料
N, X, Z = map(int, input().split())
rest_points = list(map(int, input().split()))
roads = [tuple(map(int, input().split())) for _ in range(N)]

find_shortest_path(N, X, Z, rest_points, roads)