#Raise this if generic error in calculator, DON'T FORGET TO IMPORT!
class CalcError(Exception):
    def __init__(self,*args):
        Exception.__init__(self,*args)
