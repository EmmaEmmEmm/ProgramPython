score = []
total = 0

# 第1局處理
for i in range(2):  # 最多兩次投球
    a = int(input(f"第1局第{i+1}球分數: "))
    score.append(a)
    if a == 10:  # Strike，跳出
        print("Strike! 跳過第2球，進入下一局。")
        break

# 第2局處理
for i in range(2):  # 最多兩次投球
    a = int(input(f"第2局第{i+1}球分數: "))
    score.append(a)

# 第3局處理
for i in range(2):  # 最多兩次投球
    a = int(input(f"第3局第{i+1}球分數: "))
    score.append(a)
    if a == 10:  # Strike，進行額外投球
        print("Strike! 進行額外投球。")
        for j in range(2):  # 最多兩次額外投球
            extra = int(input(f"額外投球第{j+1}球分數: "))
            score.append(extra)
        break  # 第3局Strike後，額外投球結束

# 若第3局是spare，額外投球
if score[-1] + score[-2] == 10 and score[-3] != 10:
    extra = int(input("Spare後的額外投球分數: "))
    score.append(extra)

# 計算總分
# 第1局
if score[0] == 10:  # Strike
    total += 10 + score[1] + score[2]  # 加上後面兩球的分數
elif score[0] + score[1] == 10:  # Spare
    total += 10 + score[2]  # 加下一球的分數
else:  # 沒有Strike也沒有Spare
    total += score[0] + score[1]

# 第2局
if score[2] == 10:  # Strike
    total += 10 + score[3] + score[4]  # 加上後面兩球的分數
elif score[2] + score[3] == 10:  # Spare
    total += 10 + score[4]  # 加下一球的分數
else:  # 沒有Strike也沒有Spare
    total += score[2] + score[3]

# 第3局
total += sum(score[4:])  # 第3局及額外投球直接加總

# 輸出結果
print("總分:",total)
