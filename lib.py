try:

except ModuleNotFoundError:
    try


#Check if the user is using the correct version of python. If the version is not higher than 3.6.5, the program will exit.
if sys.version_info < (3,6,5):
    print("You are not using the correct version of python. Please use version 3.6.5 or higher.")
    m.m_error
    m.doCreateFile(t.time(), type=m.m_error(type="version"))
    sys.exit()

#Check if the user is using the correct version of pip. If the version is not higher than 3, the program will exit.
if pip.__version__ < 3:
    print("You are not using the correct version of pip. Please use version 3 or higher.")
    m.m_error
    m.doCreateFile(t.time(), type=m.m_error(type="version"))
    sys.exit()
