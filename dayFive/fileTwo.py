'''
    Automatically closes the one control comes out of block
    safe for exceptions(auto-close)
    cleaner syntax
'''
with open('fileTwo.py') as ft:
    text = ft.read()
    print(text)
