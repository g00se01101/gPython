from os.path import expanduser
from bitcoinrpc.authproxy import AuthServiceProxy

# access home directory
home = expanduser("~")
access = AuthServiceProxy("http://USIv0Xm1GTsvczuYXZvS02dfIhtsm:aiRMIuPIhI82ralBzAQu1AzZoX9qy@127.0.0.1:8332")

def unlockWallet():
    "Will prompt the user to unlock wallet with encryption password."
    x = 0;
    locktime = 360;
    while True:
        try:
            x = x + 1;
            if x == 4:
                break;
            print("Attempt #%s " % (x));
            passphrase = str(raw_input("Please Enter the Wallet Passphrase: "));
            access.walletpassphrase(passphrase, locktime);
            print("Wallet successfully unlocked for %s seconds" % locktime);
            break;
        except:
            y = 3 - x;
            print ("Oops! That password is incorrect. %s attempts remain..." % y);
    return;

def generateNewAddress(numbernewaddresses):
    "Will generate new addresses, up to 100 at a time"
    #numbernewaddresses = raw_input("Generate Address(es) - Max 100: ");
    numbernewaddresses = int(numbernewaddresses);
    if int(numbernewaddresses) > 100:
            print("Too many!");
            exit();
            
    keypool = [0 for i in range(numbernewaddresses)]

    for count in range (0, numbernewaddresses):
            newAddress = access.getnewaddress();
            keypool[count] = newAddress;
            print("Address %s: %s" % (count+1, keypool[count]));
    return keypool

def createMultiSig(n,m):
    "n of m muiltisig"
    multiAddresses = generateNewAddress(m);
    print("%s of %s Multi Sig Address being created." % (n, m));
    #for i in (0, m):
    #print(multiAddresses[1]);    
    #multisig = access.createmultisig(n,m);
    print(multisig);
    return multisig['address'];


def main():
    #unlockWallet();
    n = 3;
    m = 5;
    print("Multisig Address: %s" % createMultiSig(n , m));

main()




