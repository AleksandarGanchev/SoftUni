import re

line = input()
pattern = r'((www\.)([A-Za-z0-9\-]+)(\.[a-z]+)+)'
while line:
        matches = re.search(pattern,line)
        if matches:
            print(matches.group(0))

        line = input()
