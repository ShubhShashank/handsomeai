import os

def initEvent():
    print "Initializing..."
    global current_os_dir
    global current_local_dir
    global input_def
    global pkglist
    global os
    global pmgr
    import os
    import pmgr
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
    elif console_input == "ai":
        pass
    else:
        pkg_found = "null"
        if os.path.isfile('pkg/%s/main.py' % console_input):
            os.system('python pkg/%s/main.py' % console_input)
            pkg_found = True
        if pkg_found != True:
            print "Unknown command or executable package"
