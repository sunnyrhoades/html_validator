#!/bin/python3

def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    #tags  = _extract_tags(html)
    #print(tags)

    tags = []

    for i in range(len(html)):
        if html[i] == "<":
            tag = ""
            i += 1
            while (html[i] != ">" and html[i] != " ") and i <= len(html):
                tag += html[i]
                i += 1
            tags.append(tag)

    valid_html = []
    s = []
    for tag in tags:
        if tag[0] != "/":
            if tag not in valid_html:
                valid_html.append(tag)
            s.append(tag)
        else: 
            if s == []:
                return
            last_tag = s.pop()
            if ("/" + last_tag) == tag:
                continue
            else:
                return
    if s==[]:
        return True
    else:
        return False

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []

    for i in range(len(html)):
        if html[i] == "<":
            tag = ""
            i += 1
            while (html[i] != ">" and html[i] != " ") and i <= len(html):
                tag += html[i]
                i += 1
            tags.append("<"+tag+">")
    return tags
