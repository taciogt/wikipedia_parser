__author__ = 'tacio'

import re


def escape_markup(text, match):
    begin_tag = '<nowiki>'
    end_tag = '</nowiki>'
    if re.search(begin_tag, text[:match.start()]) and re.search(end_tag, text[match.end():]):
        return True
    return False


def format_bold(text):
    pattern = "'''[^']*'''"
    matches = re.finditer(pattern, text)
    for match in matches:
        matched_str = match.group()
        if not escape_markup(text, match):
            text = text.replace(matched_str, matched_str[3:-3])
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
    pattern = "<strike>.*?</strike>"
    matches = re.finditer(pattern, text)
    for match in matches:
        matched_str = match.group()
        if not escape_markup(text, match):
            text = text.replace(matched_str, matched_str[8:-9])
    return text


def format_escape_markup(text):
    pattern = re.compile("<nowiki>.*</nowiki>")
    for match in pattern.findall(text):
        text = text.replace(match, match[8:-9])
    return text


def get_text(text):
    pattern = "(<text.*?>).*(</text>)"
    match = re.search(pattern, text)
    if match:
        text = match.group()
        text = text.replace(match.group(1), '')
        text = text.replace(match.group(2), '')
    return text


def format_level(text):
    pattern = "==.*?=="
    matches = re.finditer(pattern, text)
    for match in matches:
        matched_str = match.group()
        if not escape_markup(text, match):
            text = text.replace(matched_str, matched_str[2:-2])
    return text


def format_text(text):
    formatted_text = get_text(text)
    formatted_text = format_bold(formatted_text)
    formatted_text = format_italic(formatted_text)
    formatted_text = format_strike(formatted_text)
    formatted_text = format_level(formatted_text)
    formatted_text = format_escape_markup(formatted_text)


    return formatted_text