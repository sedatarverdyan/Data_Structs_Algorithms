# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
def anagram(S1, S2):
    if len(S1) != len(S2):
        return False
    
    dict = {}
    for i in S1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    
    for i in S2:
        if i not in dict or dict[i] == 0:
            return False
        dict[i] -= 1

    
    for value in dict.values():
        if value != 0:
            return False

    return True

print(anagram("anagram", "nagaram"))  
print(anagram("rat", "car"))          
print(anagram("heart", "earth"))      
