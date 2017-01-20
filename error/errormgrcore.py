def unknown(what):
    what_str = str(what)
    try:
        what
    except StopIteration:
        print "Error 101 - StopIteration"
    except SystemExit:
        print "Error 102 - SystemExit"
