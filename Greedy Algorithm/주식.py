from sys import stdin
readl = stdin.readline


def solution_fail(n, scores):
    today = 0
    earning = []
    result = 0

    for idx, score in enumerate(scores):
        if idx != n-1:
            if today < score:
                earning.append(score)
                today = score
            # today > tomorrow
            elif today > score:
                for i in earning:
                    if today - i > 0:
                        result += (today - i)
                today = score
                earning = []
                earning.append(today)
            # today == tomorrow
            else:
                earning.append(score)
                today = score
        else:
            today = score
            for i in earning:
                if today - i > 0:
                    result += (today - i)

    return result


def solution(n, scores):
    result = 0
    max_val = 0
    scores.reverse()

    for score in scores:
        if score > max_val:
            max_val = score
        else:
            result += (max_val - score)

    return result


if __name__ == "__main__":
    t = int(readl())
    for _ in range(t):
        n = int(readl())
        scores = list(map(int, readl().split()))
        print(solution(n, scores))
