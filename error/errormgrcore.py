def unknown(what):
    what_str = str(what)
    try:
        what
    except AssertionError:
        print "Error 101 - AssertionError"
    except AttributeError:
        print "Error 102 - AttributeError"
    except EOFError:
        print "Error 103 - EOFError"
    except FloatingPointError:
        print "Error 104 - FloatingPointError"
    except GeneratorExit:
        print "Error 105 - GeneratorExit"
    except IOError:
        print "Error 106 - IOError"
    except ImportError:
        print "Error 107 - ImportError"
    except IndexError:
        print "Error 108 - IndexError"
    except KeyError:
        print "Error 109 - KeyError"
    except KeyboardInterrupt:
        print "Error 110 - KeyboardInterrupt"
        print "Type exit to exit"
        print "Type -exit- to force exit ai"
    except MemoryError:
        print "Error 111 - MemoryError"
    except NameError:
        print "Error 112 - NameError"
    except NotImplementedError:
        print "Error 113 - NotImplementedError"
    except OSError:
        print "Error 114 - OSError"
    except OverflowError:
        print "Error 115 - OverflowError"
    except ReferenceError:
        print "Error 116 - ReferenceError"
    except RuntimeError:
        print "Error 117 - RuntimeError"
    except StopIteration:
        print "Error 118 - StopIteration"
    except SyntaxError:
        print "Error 119 - SyntaxError"
    except SystemError:
        print "Error 120 - SystemError"
    except SystemExit:
        print "Error 121 - SystemExit"
    except TypeError:
        print "Error 122 - TypeError"
    except UnboundLocalError:
        print "Error 123 - UnboundLocalError"
    except UnicodeError:
        print "Error 124 - UnicodeError"
    except ValueError:
        print "Error 125 - ValueError"
    except WindowsError:
        print "Use linux"
    except ZeroDivisionError:
        print "Error 126 - ZeroDivisionError"
    except Warning:
        print "Warning - Some Warning"

def unknownReturn(what):
    what_str = str(what)
    try:
        what
    except AssertionError:
        return "Error 101 - AssertionError"
    except AttributeError:
        return "Error 102 - AttributeError"
    except EOFError:
        return "Error 103 - EOFError"
    except FloatingPointError:
        return "Error 104 - FloatingPointError"
    except GeneratorExit:
        return "Error 105 - GeneratorExit"
    except IOError:
        return "Error 106 - IOError"
    except ImportError:
        return "Error 107 - ImportError"
    except IndexError:
        return "Error 108 - IndexError"
    except KeyError:
        return "Error 109 - KeyError"
    except KeyboardInterrupt:
        return "Error 110 - KeyboardInterrupt"
    except MemoryError:
        return "Error 111 - MemoryError"
    except NameError:
        return "Error 112 - NameError"
    except NotImplementedError:
        return "Error 113 - NotImplementedError"
    except OSError:
        return "Error 114 - OSError"
    except OverflowError:
        return "Error 115 - OverflowError"
    except ReferenceError:
        return "Error 116 - ReferenceError"
    except RuntimeError:
        return "Error 117 - RuntimeError"
    except StopIteration:
        return "Error 118 - StopIteration"
    except SyntaxError:
        return "Error 119 - SyntaxError"
    except SystemError:
        return "Error 120 - SystemError"
    except SystemExit:
        return "Error 121 - SystemExit"
    except TypeError:
        return "Error 122 - TypeError"
    except UnboundLocalError:
        return "Error 123 - UnboundLocalError"
    except UnicodeError:
        return "Error 124 - UnicodeError"
    except ValueError:
        return "Error 125 - ValueError"
    except WindowsError:
        return "Use linux"
    except ZeroDivisionError:
        return "Error 126 - ZeroDivisionError"
    except Warning:
        return "Warning - Some Warning"
