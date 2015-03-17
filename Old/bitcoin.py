from bitcoinrpc.authproxy import AuthServiceProxy

access = AuthServiceProxy("http://USIv0Xm1GTsvczuYXZvS02dfIhtsmr:aiRMIuPIhI82ralBzAQu1AzZoX9qyy@127.0.0.1:8332")

numbernewaddresses = input("Generate Addresses - Max 10: ")

if int(numbernewaddresses) > 10:
        print("Too many!")
        exit()
        
keypool = [0 for i in range(numbernewaddresses)]

for count in range (0, numbernewaddresses):

	newAddress = access.getnewaddress()
	
        keypool[count] = newAddress

	print("Address %s: %s" % (count+1, keypool[count]))





#info = access.getinfo()
#print(info)
#multiSig = access.createmultisig( 2 [key0,key1,key2])
#print("Block Info", access.getblock(bbh))
#print("MultiSig Address", multiSig)



		
"""
bestblockhash = access.getbestblockhash()

print("Connection Count", access.getconnectioncount())
print "Block Count %s" % access.getblockcount()

print "Current Block Height: %s" % (info['blocks'])
print "# of Connections: %s" % (info['connections'])
print "Current Wallet Balance: %s" % (info['balance'])            
print "Best Block Hash: %s" % (bestblockhash)
"""

