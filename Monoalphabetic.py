#Ritom Gupta, PB40-B3, T.Y B.Tech CSE
def keymap_replace(string:str, mappings:dict,lower_keys=False,lower_values=False,lower_string=False)->str:
    replaced_string=string.lower() if lower_string else string
    replaced_string=''.join(mappings.get(char,char) for char in str)
    return replaced_string

def keymap_rev_replace(string:str, mappings:dict,lower_keys=False,lower_values=False,lower_string=False)->str:
    replaced_string=string.lower() if lower_string else string
    res={v:k for k,v in mappings.items()}
    replaced_string=''.join(res.get(char,char) for char in str)
    return replaced_string

str=input("Enter your string:")
dict={"a":"b","c":"d","b":"z","e":"r"}
print(keymap_replace(str,dict,lower_keys=False,lower_values=False,lower_string=True))
str=input("Enter encoded message:")
print(keymap_rev_replace(str,dict,lower_keys=False,lower_values=False,lower_string=True))