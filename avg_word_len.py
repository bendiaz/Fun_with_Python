sentence1 = "Hi ya'll, I'm a guy from a place...what's it called? America. Ahh man."
sentence2 = "I want to learn more algos so I'm doing these things"

def solution(sentence):
    for p in "?!'.;":
        sentence = sentence.replace(p,"")
    wordz = sentence.split()
    return round(sum(len(word) for word in wordz)/len(wordz),2)


print(solution(sentence1))
print(solution(sentence2))
