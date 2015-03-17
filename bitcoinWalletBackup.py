from os.path import expanduser
from bitcoinrpc.authproxy import AuthServiceProxy

# access home directory
home = expanduser("~")
access = AuthServiceProxy("http://USIv0Xm1GTsvczuYXZvS02dfIhtsmr:aiRMIuPIhI82ralBzAQu1AzZoX9qyy@127.0.0.1:8332")

# backup wallet
print("First, you need to back up your wallet.")

backup = raw_input("Would you like to back up your wallet now?(Y/N) ")

backup = str(backup.upper())

if backup == "Y":
    access.backupwallet("%s/Desktop/wallet.backup" % home)
    print("Your wallet is backed up as 'wallet.backup' on your Desktop.")
else:
    print("Your wallet has not been backed up.")

# import from backup wallet
importWallet = raw_input("Would you like to import your wallet now?(Y/N) ")

importWallet = str(importWallet.upper())

if importWallet == "Y":
    access.importwallet("%s/Desktop/wallet.backup" % home)
    print("Your wallet has been imported from 'wallet.backup' on your Desktop.")
else:
    print("Your wallet has not been imported.")

