def install(pkg):
    import zipfile
    import urllib2
    allpkglist = open('allpkg.list', 'r')
    pkglist = open('pkg/pkg.list', 'a')
    for line in allpkglist:
        if pkg in line:
            pkgurl = line[(len(pkg)+1):]
            pkgfile = urllib2.urlopen(pkgurl)
            pkgzip = zipfil.ZipFile(pkgfile, 'r')
            pkgzip.extractall(('pkg/%s' % pkg))
            pkglist.write(pkg)
