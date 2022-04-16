import re
str = """/*
 ============================================================================
 Name        : W9T22R130006001.c
 Author      : 2130006001
 Version     : 0.1
 Copyright   : COPTLEFT
 Description : Week 9, Task 22
 ============================================================================
 */"""
pattern = re.search(r"\/\*(\s|.)*?\*\/", str, re.I)

print(hasattr(pattern, "group"))
print(pattern.group())