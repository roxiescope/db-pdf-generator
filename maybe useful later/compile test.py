import re

mylist = [["dog", "cat"], ["wildcat", "thundercat"], ["cow", "hooo"]]
r = re.compile("cat")
newlist = list(filter(r.match, mylist))  # Note 1
print(newlist)
