from bitcoinrpc.authproxy import AuthServiceProxy

access = AuthServiceProxy("http://USIv0Xm1GTsvczuYXZvS02dfIhtsmr:aiRMIuPIhI82ralBzAQu1AzZoX9qyy@127.0.0.1:8332")

x = 0
while True:
    try:
        x = x + 1
        if x == 4:
            break
        print("Attempt #%s " % (x))
        passphrase = str(raw_input("Please Enter the Wallet Passphrase: "))
        access.walletpassphrase(passphrase, 360)
        break
    except:
        y = 3 - x
        print ("Oops! That password is incorrect. %s attempts remain..." % y)
