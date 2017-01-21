import os

def initEvent():
    print "Initializing..."
    global current_os_dir
    global current_local_dir
    global input_def
    global pkglist
    global os
    global pmgr
    global error
    global sys
    global ai
    import os
    import pmgr
    import error.errormgrcore as error
    import sys
    import ai.ai as ai
    current_os_dir = os.getcwd()
    current_local_dir = "home"
    input_def = "LOCAL://" + current_local_dir + ":"
    pkglist = open('pkg/pkg.list', 'r')
    pkg_found = "null"
    print "Initialized"

initEvent()

while True:
    console_input = raw_input(input_def)
    if "pmgr install" in console_input:
        pmgr.install(console_input[12:])
    elif "pmgr uninstall" in console_input:
        pmgr.uninstall(console_input[14:])
    elif console_input == "ai":
        ai.ai()
    elif console_input == "exit":
        sys.exit()
    else:
        pkg_found = "null"
        if os.path.isfile('pkg/%s/main.py' % console_input):
            pkg_mod = __import__(('pkg.' + console_input + '.main'), fromlist=[''])
            try:
                pkg_mod.main()
            except AttributeError:
                os.system('python pkg/%s/main.py' % console_input)
            else:
                error.unknown(pkg_mod.main())
            pkg_found = True
        if pkg_found != True:
            print "Unknown command or executable package"
