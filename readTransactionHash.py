from myWeb3 import myWeb3

hashTx = '0x6e71ca52e93002dc1154c55c364dd3e935410cdf5c61c4af2d6baf3811c24abd'

w3 = myWeb3()
w3.initAccount(privateKey='dda1ec2a2312151ac7d82cb9842b72c93edcad903b44a185387cd53fd2c29625')

result = w3.getReceiptInfoFromHash(hashTx)
print(result)
