def generate_possible_answers():
    from itertools import permutations
    # 生成所有 0-9 不重複的五位數排列
    return [''.join(p) for p in permutations("0123456789", 5)]

def get_feedback(guess, answer):
    a = sum(guess[i] == answer[i] for i in range(5))
    b = sum(min(guess.count(d), answer.count(d)) for d in set(guess)) - a
    return f"{a}A{b}B"

def computer_guess():
    answer = input().strip()
    possible_answers = generate_possible_answers()

    while True:
        guess = possible_answers[0]
        feedback = get_feedback(guess, answer)
        
        if feedback == "5A0B":
            print(guess)
            break
        
        possible_answers = [
            p for p in possible_answers if get_feedback(guess, p) == feedback
        ]

computer_guess()
