import re
# str = """/*
#  ============================================================================
#  Name        : W9T22R130006001.c
#  Author      : 2130006001
#  Version     : 0.1
#  Copyright   : COPTLEFT
#  Description : Week 9, Task 22
#  ============================================================================
#  */"""
# pattern = re.search(r"\/\*(\s|.)*?\*\/", str, re.I)

str = "W11T26R130006001_YAV.c"

pattern = re.search(r"^[A-Z][0-9]+[A-Z][0-9]+[A-Z][0-9]{9}(.*)\.c$", str, re.I)

print(hasattr(pattern, "group"))
print(pattern.group())