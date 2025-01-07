caves_num, start = map(int, input().split())
caves = {}
for i in range(caves_num):
    cave, gold, path_1, path_2 = map(int, input().split())
    caves[cave] = (gold, path_1, path_2)
def find(caves, start):
    def dfs(c_cave, visited, c_gold):
        if c_cave in visited:
            return c_gold
        
        visited.add(c_cave)
        gold, path_1, path_2 = caves[c_cave]
        c_gold += gold

        if path_1 == 0 and path_2 == 0:
            visited.remove(c_cave)
            return c_gold
        max1 = dfs(path_1, visited, c_gold) if path_1 != 0 else c_gold
        max2 = dfs(path_2, visited, c_gold) if path_2 != 0 else c_gold

        visited.remove(c_cave)

        return max(max1, max2)
    return dfs(start, set(), 0)

print(find(caves, start))