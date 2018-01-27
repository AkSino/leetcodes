import re


def find_LHS(string):
    emails = re.findall(r'(?:^|(?:[->?!]\s))([a-zA-Z]+)', string[0])
    if emails:
        final = emails[0].strip()
        return (final)
    else:
        return (string[0])

print(find_LHS('Verb -> book * '))