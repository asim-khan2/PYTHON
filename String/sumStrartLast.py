def sum(str):
    s = str[:2]
    s1 = str[-2:]
    # print(s)
    # print(s1)
    # print(s+s1)
    if len(s+s1) >= 4:
        return s+s1
    else:
        return None


str = '''We use any before nouns to refer to indefinite or
unknown quantities or an unlimited entity'''
print(len(str))
print(sum(str))