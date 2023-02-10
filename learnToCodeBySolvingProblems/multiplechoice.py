# ccc11s2
numLines = int(input())
answers=[]
correctAnswers=[]

for i in range(0, numLines):
    answers.append(input())

for i in range(0, numLines):
    correctAnswers.append(input())

correct = 0
for i in range(0, numLines):
    if correctAnswers[i] == answers[i]:
        correct = correct + 1

print(correct)