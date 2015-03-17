#!/usr/bin/python

from bitcoinrpc.authproxy import AuthServiceProxy

access = AuthServiceProxy("http://username:password@127.0.0.1:8332")

def accessHomeDir():
    from os.path import expanduser
    # access home directory
    global home;
    home = expanduser("~");
    return;

def encryptWallet():
    "Set up encrypted wallet functionality"
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
    "Will generate new addresses, up to 100 at a time"
    numbernewaddresses = raw_input("Generate Address(es) - Max 100: ");
    numbernewaddresses = int(numbernewaddresses);
    if int(numbernewaddresses) > 100:
            print("Too many!");
            exit();
            
    keypool = [0 for i in range(numbernewaddresses)]

    for count in range (0, numbernewaddresses):
            newAddress = access.getnewaddress();
            keypool[count] = newAddress;
            print("Address %s: %s" % (count+1, keypool[count]));
    return

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

def backupWallet():
    # backup wallet
    print("First, you need to back up your wallet.");
    backup = raw_input("Would you like to back up your wallet now?(Y/N) ");
    backup = str(backup.upper());

    if backup == "Y":
        access.backupwallet("%s/Desktop/wallet.backup" % home);
        print("Your wallet is backed up as 'wallet.backup' on your Desktop.");
    else:
        print("Your wallet has not been backed up.");
    return;

def importWallet():
    # import wallet
    importWallet = raw_input("Would you like to import your wallet now?(Y/N) ");
    importWallet = str(importWallet.upper());
    if importWallet == "Y":
        access.importwallet("%s/Desktop/wallet.backup" % home);
        print("Your wallet has been imported from 'wallet.backup' on your Desktop.");
    else:
        print("Your wallet has not been imported.");
    return;

#accessHomeDir();
#backupWallet();
#importWallet();
#unlockWallet();
#encryptWallet();
generateNewAddress();



