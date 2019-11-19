import hashlib

str="Preeyesh"

result=hashlib.sha1(str.encode())

print("The hec equivalent of SHA1 is: ",result.hexdigest())
print("\r")