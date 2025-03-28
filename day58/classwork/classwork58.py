# classwork 1
def lottery(s):
    result = []
    seen = set()  

    for i in range(len(s)):  
        if s[i].isdigit() and s[i] not in seen:
            result.append(s[i])
            seen.add(s[i])  

    return ''.join(result) if result else "One more run!"

# classwork 2
def longest_word(string_of_words):
    # Give me back the longest word!
    words = string_of_words.split()
    longest = ""
    
    for word in words:
        if len(word) >= len(longest): 
            longest = word
    
    return longest

    pass

