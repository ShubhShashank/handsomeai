def install(pkg):
    import zipfile
    import urllib2
    pkglist = open('pkg/pkg.list', 'a')
    user = raw_input("Uploader's Username: ")
    pkgurl = "https://github.com/" + user + "/" + pkg + "/zip/master"
    pkgfile = urllib2.urlopen(pkgurl)
    pkgzip = zipfile.ZipFile(pkgfile, 'r')
    pkgzip.extractall(('pkg/%s' % pkg))
    pkglist.write(pkg)

def uninstall(pkg):
    sure = raw_input("Are you sure you want to delete %s (Y/N): " % pkg)
    if sure == "Y":
        import shutil
        import os
        shutil.rmtree(('pkg/' + pkg))
        pkglist = open('pkg/pkg.list', 'r')
        pkglist_lines = pkglist.readlines()
        pkglist.close()
        os.remove('pkg/pkg.list')
        pkglist = open('pkg/pkg.list', 'w')
        for line in pkglist_lines:
            if line != pkg:
                pkglist.write(line)
        pkglist.close()
    else:
        print ("Understood, wont delete %s" % pkg)

def update():
    import urllib2
    import zipfile
    pkglist = open('pkg/pkg.list', 'r')
    for line in pkglist:
        update = open(('pkg/%s/update' % line), 'r')
        pkgfile = urllib2.urlopen(update)
        pkgzip = zipfile.ZipFile(pkgfile, 'r')
        shutil.rmtree(('pkg/%s' % line))
        pkgzip.extractall(('pkg/%s' % line))
        update.close()
