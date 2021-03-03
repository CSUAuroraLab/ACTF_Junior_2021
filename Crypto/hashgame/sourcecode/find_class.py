import re

find_class = "warnings.catch_warnings"

with open("C:/Users/lenovo/Desktop/flag.txt", "r") as f:
    content = f.read()
    pattern = re.compile(r"<class '(.*?)'>")
    result = pattern.findall(content)
    print(result)
    j = 0
    for i in result:
        if find_class in i:
            print(i)
            print(j)
            break
        else:
            j = j + 1 
