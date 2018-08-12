import sys

def ispythonversion(version):
    if float(sys.version[:3]) >= version:
        return True
    else:
        return False

if not ispythonversion(2.6):
    print "You are running Python version", sys.version[:3], ", version 2.6 or 2.7 is required. Please update. Aborting..."
    exit()


