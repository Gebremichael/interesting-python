# enter two words,
# if they share a character,
# the words are displayed in a interesting way

def main():
    word1,word2 = input().upper().split()

    if len(word1)>len(word2):
        word1,word2=word2,word1

    for c in word1:
        if c in word2: break


    if c not in word2:
        print("NO COMMON CHARACTER FOUND")
        exit()

    i,I = word1.find(c), word2.find(c)

    for k,C in enumerate(word1):
        print(*[" "]*I+[C] if k!=i else word2)

if __name__=="__main__":
    main()