from myWeb3 import myWeb3

hashTx = '0x807baf5eb1d6f9e1799f1c29a428ee5574f8f5a931b6d9eeb312c7b620471d29'

w3 = myWeb3()
w3.initAccount(privateKey='dda1ec2a2312151ac7d82cb9842b72c93edcad903b44a185387cd53fd2c29625')

result = w3.getReceiptInfoFromHash(hashTx)
print(result)
