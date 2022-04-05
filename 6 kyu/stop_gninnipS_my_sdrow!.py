def spin_words(sentence):
    
    arr = []
    
    for i in sentence.split(" "):
        if len(i) >= 5:
            i = i[::-1]
            
        arr.append(i)
    
    return " ".join(arr)
