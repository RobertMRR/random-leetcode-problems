def calPoints(operations) -> int:
    scores = []
    for item in operations:
        print(f"scores are: {scores}")
        if item == "+":
            scores.append(int(scores[-2] + scores[-1]))
        elif item == "D":
            scores.append(int(scores[-1]) * 2)
        elif item == "C":
            scores.pop()
        else:
            scores.append(int(item))
    total = 0
    for score in scores:
        total += int(score)
    return total

print(calPoints(["5","-2","4","C","D","9","+","+"]))