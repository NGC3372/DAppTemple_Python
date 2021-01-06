from myWeb3 import myWeb3

w3 = myWeb3()
w3.initAccount(privateKey='dda1ec2a2312151ac7d82cb9842b72c93edcad903b44a185387cd53fd2c29625')

print(w3.getBalance('0x76e0eC050466c4dddBbAA25C3f069C18F026AF95'))
