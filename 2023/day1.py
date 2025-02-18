import re; print(sum(int(a + b) for a, b in re.findall(r'(\d).*?(\d)', open("day1input.txt").read())))
