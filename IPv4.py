import re
def IPv4(input_str: str) -> bool:
    if re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$").match(input_str) == False:
        return False
    chars = re.split('\.', input_str)
    for i in range(0, 4):
        if chars[i].isdigit() == False:
            return False
        elif int(chars[i]) > 255:
            return False
    return True
print(IPv4(input()))