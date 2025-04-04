grade_input = input().strip()
grade = grade_input[0]
level = grade_input[1] if len(grade_input) > 1 else ''
grade_ = ['D','C','B','A']
score = 0.0
for i in range(4):
    if grade == grade_[i]:
        score += i+1.0
        if level == '+':
            score += 0.3
        elif level == '-':
            score -= 0.3
print(score)