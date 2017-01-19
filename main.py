import os
import time

def InitEvent():
    print "Initializing"
    init_start_time = time.time()
    global current_os_dir
    global current_local_dir
    global input_def
    global pkglist
    current_os_dir = os.getcwd()
    current_local_dir = "home"
    input_def = "LOCAL://" + current_local_dir + ":"
    pkglist = open('pkg/pkg.list', 'r')
    pkg_found = "null"
    init_time = time.time() - init_start_time
    print "Initialized in " + str(pre_init_time)

preInitEvent()

while True:
    console_input = raw_input(input_def)
    if console_input == "install":
        pass
    elif console_input == "ai":
        pass
    else:
        pkg_found = "null"
        if os.path.isfile('pkg/%s/main.py' % console_input):
            os.system('python pkg/%s/main.py' % console_input)
            pkg_found = True
        else:
            print "Package is not executable"
            pkg_found = True
        if pkg_found != True:
            print "Unknown command or executable package"
