def main(what):
    try:
        what
    except UserWarning:
        return "Warning - User Warning"
    except DeprecationWarning:
        return "Warning - Deprecation Warning"
    except PendingDeprecationWarning:
        return "Warning - Pending Deprecation Warning"
    except SyntaxWarning:
        return "Warning - Syntax Warning"
    except RuntimeWarning:
        return "Warning - Runtime Warning"
    except ImportWarning:
        return "Warning - Import Warning"
    except UnicodeWarning:
        return "Warning - Unicode Warning"
