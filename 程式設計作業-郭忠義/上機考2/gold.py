def find(caves, start):
    def dfs(c_cave, visited, c_gold):
        if c_cave in visited:
            return c_gold
        visited.add(c_cave)
        gold, path_1, path_2 = caves[c_cave]

        c_gold += gold

        if path_1 == 0 and path_2 ==0:
            # visited.remove(c_cave)
            return c_gold
        max_path_1 = dfs(path_1, visited, c_gold) if path_1 != 0 else c_gold

        max_path_2 = dfs(path_2, visited, c_gold) if path_2 != 0 else c_gold

        visited.remove(c_cave)
        return max(max_path_1, max_path_2)
    return dfs(start, set(), 0)
cave_num, start_cave = map(int, input().split())

caves = {}
for i in range(cave_num):
    cave, gold, path_1, path_2 = map(int, input().split())
    caves[cave] = (gold, path_1, path_2)

print(find(caves, start_cave))