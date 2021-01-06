from myWeb3 import myWeb3


def setCaller_storageContract(address):
    w3 = myWeb3()
    w3.initAccount(privateKey='dda1ec2a2312151ac7d82cb9842b72c93edcad903b44a185387cd53fd2c29625')
    contractAddress = '0x26AAA1C996324a56F2755726cAC15FEaA618FD21'
    abi_file = open('compiler/abi_storage', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'setCaller')
    hashTx = w3.transcationContractFunction(function(address))
    print(hashTx)


def setCaller_manageContract():
    w3 = myWeb3()
    w3.initAccount(privateKey='dda1ec2a2312151ac7d82cb9842b72c93edcad903b44a185387cd53fd2c29625')
    contractAddress = '0x52B49a8DF0F9A03C0a35BC5c8Db3e7888B60E400'
    abi_file = open('compiler/abi_manage', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'setCaller')
    hashTx = w3.transcationContractFunction(function('0x61bEa2058e8d5a01F1f9898E49F53Cc3cc8E6520'))
    print(hashTx)


def setCaller_tableContract():
    w3 = myWeb3()
    w3.initAccount(privateKey='dda1ec2a2312151ac7d82cb9842b72c93edcad903b44a185387cd53fd2c29625')
    contractAddress = '0x489F157C67583cF895F9011783422f421F8D85bD'
    abi_file = open('compiler/abi_table', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'setCaller')
    hashTx = w3.transcationContractFunction(function('0x61bEa2058e8d5a01F1f9898E49F53Cc3cc8E6520'))
    print(hashTx)


def setCaller_secretContract():
    w3 = myWeb3()
    w3.initAccount(privateKey='dda1ec2a2312151ac7d82cb9842b72c93edcad903b44a185387cd53fd2c29625')
    contractAddress = '0xCA0D34C770835A58340CC7731b484c0Ae1e9a2d6'
    abi_file = open('compiler/abi_secret', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'setCaller')
    hashTx = w3.transcationContractFunction(function('0x61bEa2058e8d5a01F1f9898E49F53Cc3cc8E6520'))
    print(hashTx)


def setDataStorageContractAddress_tableContract():
    w3 = myWeb3()
    w3.initAccount(privateKey='0d64c5cd990153ce7d79ab5a0c4255b9f34ea17862ded1bd53f4408eb6ebe4d9')
    contractAddress = '0x489F157C67583cF895F9011783422f421F8D85bD'
    abi_file = open('compiler/abi_table', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'setDataStorageContractAddress')
    hashTx = w3.transcationContractFunction(function('0x26AAA1C996324a56F2755726cAC15FEaA618FD21'))
    print(hashTx)


def setDataManageContractAddress_tableContract():
    w3 = myWeb3()
    w3.initAccount(privateKey='0d64c5cd990153ce7d79ab5a0c4255b9f34ea17862ded1bd53f4408eb6ebe4d9')
    contractAddress = '0x489F157C67583cF895F9011783422f421F8D85bD'
    abi_file = open('compiler/abi_table', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'setDataManageContractAddress')
    hashTx = w3.transcationContractFunction(function('0x52B49a8DF0F9A03C0a35BC5c8Db3e7888B60E400'))
    print(hashTx)


def setSecretContractAddress_tableContract():
    w3 = myWeb3()
    w3.initAccount(privateKey='0d64c5cd990153ce7d79ab5a0c4255b9f34ea17862ded1bd53f4408eb6ebe4d9')
    contractAddress = '0x489F157C67583cF895F9011783422f421F8D85bD'
    abi_file = open('compiler/abi_table', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'setScecrtKeyContractAddress')
    hashTx = w3.transcationContractFunction(function('0xCA0D34C770835A58340CC7731b484c0Ae1e9a2d6'))
    print(hashTx)

def setTableContractAddress_manageContract(address):
    w3 = myWeb3()
    w3.initAccount(privateKey='0d64c5cd990153ce7d79ab5a0c4255b9f34ea17862ded1bd53f4408eb6ebe4d9')
    contractAddress = '0x52B49a8DF0F9A03C0a35BC5c8Db3e7888B60E400'
    abi_file = open('compiler/abi_manage', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'setTableContractAddress')
    hashTx = w3.transcationContractFunction(function(address))
    print(hashTx)


def setPublicData_manageContract(dataName, dataContent):
    w3 = myWeb3()
    w3.initAccount(privateKey='0d64c5cd990153ce7d79ab5a0c4255b9f34ea17862ded1bd53f4408eb6ebe4d9')
    contractAddress = '0x52B49a8DF0F9A03C0a35BC5c8Db3e7888B60E400'
    abi_file = open('compiler/abi_manage', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'setPublicData')
    hashTx = w3.transcationContractFunction(function(dataName, dataContent))
    print(hashTx)

def setUserData_manageContract(dataName, dataContent):
    w3 = myWeb3()
    w3.initAccount(privateKey='0d64c5cd990153ce7d79ab5a0c4255b9f34ea17862ded1bd53f4408eb6ebe4d9')
    contractAddress = '0x52B49a8DF0F9A03C0a35BC5c8Db3e7888B60E400'
    abi_file = open('compiler/abi_manage', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'setUserData')
    hashTx = w3.transcationContractFunction(function(dataName, dataContent))
    print(hashTx)


def createData_DHKey_SecretContract(dataName, managerKey):
    w3 = myWeb3()
    w3.initAccount(privateKey='0d64c5cd990153ce7d79ab5a0c4255b9f34ea17862ded1bd53f4408eb6ebe4d9')
    contractAddress = '0xCA0D34C770835A58340CC7731b484c0Ae1e9a2d6'
    abi_file = open('compiler/abi_secret', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'createData_DHKey')
    hashTx = w3.transcationContractFunction(function(dataName, managerKey))
    print(hashTx)


def addUser_DHKey_SecretContract(dataName, userKey):
    w3 = myWeb3()
    w3.initAccount(privateKey='0d64c5cd990153ce7d79ab5a0c4255b9f34ea17862ded1bd53f4408eb6ebe4d9')
    contractAddress = '0xCA0D34C770835A58340CC7731b484c0Ae1e9a2d6'
    abi_file = open('compiler/abi_secret', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contractAddress, abi, 'addUser_DHKey')
    hashTx = w3.transcationContractFunction(function(dataName, userKey))
    print(hashTx)


if __name__ == '__main__':
    #setCaller_storageContract('0x52B49a8DF0F9A03C0a35BC5c8Db3e7888B60E400')
    #setCaller_manageContract()
    #setCaller_tableContract()
    #setDataStorageContractAddress_tableContract()
    #setTableContractAddress_manageContract('0x489F157C67583cF895F9011783422f421F8D85bD')
    #setPublicData_manageContract('data1', 'QmXbkFEXT5e4Dm4x1dswmo9gFL6WbyJroJURw4TAgNxfmA')
    #setCaller_secretContract()
    #createData_DHKey_SecretContract('dataTest', 'QmaLdxhUsvUzu35YDyJ3qpCX8xLJuUXuX7LULZfksPiZkM')
    #addUser_DHKey_SecretContract('dataTest', 'QmfRvoSPqAmmonFQhobRc1QAwD9gU3rrjSHUir1ANzX66v')
    #setUserData_manageContract('user1', 'QmU5k7ter3RdjZXu3sHghsga1UQtrztnQxmTL22nPnsu3g')
    #setDataManageContractAddress_tableContract()
    setSecretContractAddress_tableContract()
