#Ritom Gupta, PB40-B3, T.Y B.Tech CSE
from string import ascii_letters,digits
from random import shuffle

def keymap_replace(string:str, mappings:dict,lower_keys=False,lower_values=False,lower_string=False)->str:
    replaced_string=string.lower() if lower_string else string
    replaced_string=''.join(mappings.get(char,char) for char in str)
    return replaced_string

def keymap_rev_replace(string:str, mappings:dict,lower_keys=False,lower_values=False,lower_string=False)->str:
    replaced_string=string.lower() if lower_string else string
    res={v:k for k,v in mappings.items()}
    replaced_string=''.join(res.get(char,char) for char in str)
    return replaced_string

def generate_substitution():
    pool=ascii_letters+digits
    original_pool=list(pool)
    shuffled_pool = list(pool)
    shuffle(shuffled_pool)
    return dict(zip(original_pool,shuffled_pool))

str=input("Enter your string:")
dict=generate_substitution()
print(keymap_replace(str,dict,lower_keys=False,lower_values=False,lower_string=True))
str=input("Enter encoded message:")
print(keymap_rev_replace(str,dict,lower_keys=False,lower_values=False,lower_string=True))

# Enter your string:the quick brown fox jumps Over th3 lazy dog
# 9BE SAa1L eKQ70 dQt mA4cM FUEK 9Bb 2q8P uQv
# Enter encoded message:9BE SAa1L eKQ70 dQt mA4cM FUEK 9Bb 2q8P uQv
# the quick brown fox jumps Over th3 lazy dog
#
# Process finished with exit code 0