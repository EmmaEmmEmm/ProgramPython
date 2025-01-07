from collections import defaultdict

def find_max_gold(n, start_cave, cave_data):
    def dfs(current_cave, current_gold, visited):
        # 如果已經走過這個山洞，結束搜尋
        if current_cave in visited:
            return current_gold

        # 更新當前黃金總數
        current_gold += cave_data[current_cave]["gold"]
        visited.add(current_cave)

        # 找到下一步可以前往的山洞
        next_cave1 = cave_data[current_cave]["next1"]
        next_cave2 = cave_data[current_cave]["next2"]

        # 如果下一步是空的山洞，結束搜尋
        if next_cave1 == 0 and next_cave2 == 0:
            return current_gold

        # 遞迴搜尋每個可能的下一步，取最大值
        max_gold1 = dfs(next_cave1, current_gold, set(visited)) if next_cave1 != 0 else current_gold
        max_gold2 = dfs(next_cave2, current_gold, set(visited)) if next_cave2 != 0 else current_gold

        return max(max_gold1, max_gold2)

    # 開始搜尋，從起始山洞進入
    return dfs(start_cave, 0, set())

# 讀取輸入資料
n, start_cave = map(int, input().split())
cave_data = defaultdict(dict)

for _ in range(n):
    cave_id, gold, next1, next2 = map(int, input().split())
    cave_data[cave_id] = {"gold": gold, "next1": next1, "next2": next2}

# 計算最多黃金數量
max_gold = find_max_gold(n, start_cave, cave_data)
print(max_gold)