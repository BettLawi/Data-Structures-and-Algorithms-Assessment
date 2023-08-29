def word_frequency(sentence):
        words = sentence.lower().split()
        word_count = {}
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] +=1
        return word_count        

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)    




