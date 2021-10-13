import re


def getUserReference(text):
    pattern = re.compile(r"\B@\w*")
    return pattern.findall(text)
