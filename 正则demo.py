import re
content = "hello 1234567 this a  demo"
resault = re.match("^hello\s(\d+)\sthis.*demo$", content)
print(resault)
print(resault.group(1))
print(resault.span())

content = "hello 123456 world this a demo" \
          "thank you"
res = re.match("^he.*?(\d+).*?you$", content, re.S)
print(res.group(1))

content = "today happy hello 1234567 this a  demo"
res1 = re.search("he.*?(\d+).*?demo", content)
print(res1)
print(res1.group(1))
