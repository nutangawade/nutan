
def fre( a):
    freq={}
    for char in a:
        if char.isalpha():
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
    return freq

sentence=input("Enter a sentence:")
print("Frequency of letter:")
print(fre(sentence))
