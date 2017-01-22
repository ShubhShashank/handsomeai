import os

def main():
    clist = []
    if os.path.isfile('calc.py'):
        calc = __import__('calc', fromlist=[''])
        clist.extend(calc.main())
        return clist
    else:
        return 0
