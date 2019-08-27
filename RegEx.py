import re

txt = "this is spain"
# print(re.findall("that", txt))
# x = re.sub('\s',"--", txt, 1)
x = re.search(r"\bs\w+", txt)
print(x.string)
