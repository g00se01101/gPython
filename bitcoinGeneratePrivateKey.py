from os.path import expanduser
from bitcoinrpc.authproxy import AuthServiceProxy

# access home directory
home = expanduser("~")
access = AuthServiceProxy("http://USIv0Xm1GTsvczuYXZvS02dfIhtsmr:aiRMIuPIhI82ralBzAQu1AzZoX9qyy@127.0.0.1:8332")

#access.walletpassphrase("apple", 360)

def printme( str ):
    "This prints a passed string into this function"
    print str
    return

printme("I'm first");
printme("Again second");
