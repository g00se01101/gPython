#!/usr/bin/python

from bitcoinrpc.authproxy import AuthServiceProxy

access = AuthServiceProxy("http://USIv0Xm1GTsvczuYXZvS02dfIhtsmr:aiRMIuPIhI82ralBzAQu1AzZoX9qyy@127.0.0.1:8332")

def encryptWallet():
    "Set Up Wallet Encryption: "
    encryptcheck = raw_input("Would you like to encrypt your wallet now?(Y/N) ");
    encryptcheck = str(encryptcheck.upper());
    #print("Decision: %s" % encryptcheck );

    if encryptcheck == "Y":
        print("Please WRITE this password down. This is money we are talking about!");
        passphrase = raw_input("Enter Password to Encrypt Wallet: " );
        confirmpass = raw_input("Please re-enter Password to confirm match: " );
        match = (passphrase == confirmpass);
        if match == True:
            print("Wallet Successfully Encrypted!");
            print("Your wallet encryption key is: %s" % passphrase);
            access.encryptwallet(passphrase);
        else:
            print("Passwords do not match! Please Try Again!");
            exit();
    elif encryptcheck == "N":
        print("Tread softly my friend.");
        exit();
    else:
        print("You Must Enter Y or N.");
        exit();
    return;

def generateNewAddress():
    
    numbernewaddresses = raw_input("Generate Address(es) - Max 100: ")
    numbernewaddresses = int(numbernewaddresses)
    if int(numbernewaddresses) > 100:
            print("Too many!")
            exit()
            
    keypool = [0 for i in range(numbernewaddresses)]

    for count in range (0, numbernewaddresses):
            newAddress = access.getnewaddress()
            keypool[count] = newAddress
            print("Address %s: %s" % (count+1, keypool[count]))
    return

    

#encryptWallet();
generateNewAddress();



