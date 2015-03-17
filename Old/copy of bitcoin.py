from bitcoinrpc.authproxy import AuthServiceProxy

access = AuthServiceProxy("http://USIv0Xm1GTsvczuYXZvS02dfIhtsmr:aiRMIuPIhI82ralBzAQu1AzZoX9qyy@127.0.0.1:8332")

a = access.getinfo()

for x in range(0, 3):
	newAddress = access.getnewaddress()
	print("Address", newAddress)
	if x == 0:
		key0 = newAddress 
	if x == 1:
		key1 = newAddress 
	if x == 2:
		key2 = newAddress 

print(a)

#multiSig = access.createmultisig( 2 [key0,key1,key2])

bbh = access.getbestblockhash()

print("Connection Count", access.getconnectioncount())
print("Block Count", access.getblockcount())
print("Best Block Hash", access.getbestblockhash())

#print("Block Info", access.getblock(bbh))
#print("MultiSig Address", multiSig)
print "Current Wallet Balance: ", a['balance']
print "Current Block Height: ", a['blocks']
print "# of Connections: ", a['connections']