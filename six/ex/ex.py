scores = [60, 75, 90, 65, 80]
total = 0
count = 0

for s in scores:
    if s >= 70:
        total += s
        count += 1

print(f"합계: {total}, 개수: {count}")

def check_pass(scores, standard=70):
    avg = sum(scores) / len(scores)
    if avg >= standard:
        return "합격"
    else:
        return "불합격"

name_list = []
total = 0

with open("scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, score = line.strip().split(",")
        score = int(score)
        if score >= 80:
            name_list.append(name)
            total += score

print(name_list)
print(total)