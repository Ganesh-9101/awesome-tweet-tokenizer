import re


def getEmails(text):
    pattern = re.compile("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)")
    return pattern.findall(text)
