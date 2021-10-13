import re


def getHashtags(text):
    pattern = re.compile("#+\w*[a-zA-Z]+\w*")
    return pattern.findall(text)
