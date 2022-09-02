#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following
example (tabulation before -)
You must use a with statement
"""
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8", "replace")))
