__author__ = 'tacio'

import re


def escape_markup(text, match):
    begin_tag = '<nowiki>'
    end_tag = '</nowiki>'
    if re.search(begin_tag, text[:match.start()]) and re.search(end_tag, text[match.end():]):
        return True
    return False


def format_bold(text):
    pattern = re.compile("'''[^']*'''")
    for match in pattern.findall(text):
        text = text.replace(match, match[3:-3])
    return text


def format_italic(text):
    pattern = "''[^']*''"
    matches = re.finditer(pattern, text)
    for match in matches:
        matched_str = match.group()
        if not escape_markup(text, match):
            text = text.replace(matched_str, matched_str[2:-2])
    return text


def format_strike(text):
    pattern = re.compile("<strike>.*</strike>")
    for match in pattern.findall(text):
        text = text.replace(match, match[8:-9])
    return text


def format_escape_markup(text):
    pattern = re.compile("<nowiki>.*</nowiki>")
    for match in pattern.findall(text):
        text = text.replace(match, match[8:-9])
    return text


def format_text(text):
    formatted_text = format_bold(text)
    formatted_text = format_italic(formatted_text)
    formatted_text = format_strike(formatted_text)
    formatted_text = format_escape_markup(formatted_text)

    return formatted_text