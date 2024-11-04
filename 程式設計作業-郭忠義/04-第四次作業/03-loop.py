strs = input()
strs = ''.join(filter(str.isdigit, strs))

answer = []

a = reversed(list(strs))
if list(a) == list(strs):
    for i in range(len(strs)):
        answer.append(int(strs[i]))
    print(list(set(answer)))
else:
    # 非回文
    for i in set(strs):
        if strs.count(i) > 1:
            answer.append(int(i))
    answer.sort(reverse=True)
    print(answer)