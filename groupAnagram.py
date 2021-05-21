#O(w*n*log(n) + n* w*log(w)) time | O(wn) space
#    O(wn) space || w*n*log(n)
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord= "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())

groupAnagrams(["yo","act","flop","tac","cat","oy","olfp"])
        
    
