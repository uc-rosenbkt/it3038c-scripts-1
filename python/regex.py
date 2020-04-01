import re
data = "Hello. My email is sayersmx@mail.uc.edu. Please contact me"
p = re.compile('[A-Za-z0-9.]+@[A-z0-9.]+\.[A-z0-9]{2,}')
print(p.search(data).group())