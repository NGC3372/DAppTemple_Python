from myWeb3 import myWeb3


def get_storage_contract_caller():
    w3 = myWeb3()
    contract_address = '0x26AAA1C996324a56F2755726cAC15FEaA618FD21'
    abi_file = open('compiler/abi_storage', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contract_address, abi, 'caller')
    result = w3.callContractFunction(function())
    print(result)


def get_manage_contract_caller():
    w3 = myWeb3()
    contract_address = '0x52B49a8DF0F9A03C0a35BC5c8Db3e7888B60E400'
    abi_file = open('compiler/abi_manage', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contract_address, abi, 'caller')
    result = w3.callContractFunction(function())
    print(result)


def get_secret_contract_caller():
    w3 = myWeb3()
    contract_address = '0xCA0D34C770835A58340CC7731b484c0Ae1e9a2d6'
    abi_file = open('compiler/abi_secret', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contract_address, abi, 'caller')
    result = w3.callContractFunction(function())
    print(result)

def get_storage_contract_public_data(dataName):
    w3 = myWeb3()
    contract_address = '0x26AAA1C996324a56F2755726cAC15FEaA618FD21'
    abi_file = open('compiler/abi_storage', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contract_address, abi, 'getPublicData')
    result = w3.callContractFunction(function(dataName))
    print(result)

def get_storage_contract_user_data(address, dataName):
    w3 = myWeb3()
    contract_address = '0x26AAA1C996324a56F2755726cAC15FEaA618FD21'
    abi_file = open('compiler/abi_storage', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contract_address, abi, 'getUserData')
    result = w3.callContractFunction(function(address, dataName))
    print(result)


def get_table_contract_dataStorageContractAddress():
    w3 = myWeb3()
    contract_address = '0x489F157C67583cF895F9011783422f421F8D85bD'
    abi_file = open('compiler/abi_table', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contract_address, abi, 'dataStorageContractAddress')
    result = w3.callContractFunction(function())
    print(result)


def get_table_contract_dataManageContractAddress():
    w3 = myWeb3()
    contract_address = '0x489F157C67583cF895F9011783422f421F8D85bD'
    abi_file = open('compiler/abi_table', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contract_address, abi, 'dataManageContractAddress')
    result = w3.callContractFunction(function())
    print(result)


def get_table_contract_secretContractAddress():
    w3 = myWeb3()
    contract_address = '0x489F157C67583cF895F9011783422f421F8D85bD'
    abi_file = open('compiler/abi_table', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contract_address, abi, 'scecrtKeyContractAddress')
    result = w3.callContractFunction(function())
    print(result)

def getManage_DHKey_secret_contract(dataName):
    w3 = myWeb3()
    contract_address = '0xCA0D34C770835A58340CC7731b484c0Ae1e9a2d6'
    abi_file = open('compiler/abi_secret', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contract_address, abi, 'getManage_DHKey')
    result = w3.callContractFunction(function(dataName))
    print(result)


def getUser_DHKey_secret_contract(userAddress, dataName):
    w3 = myWeb3()
    contract_address = '0xCA0D34C770835A58340CC7731b484c0Ae1e9a2d6'
    abi_file = open('compiler/abi_secret', 'r')
    abi = abi_file.read()
    abi_file.close()
    function = w3.getContractFunction(contract_address, abi, 'getUser_DHKey')
    result = w3.callContractFunction(function(userAddress, dataName))
    print(result)


if __name__ == '__main__':
    #get_manage_contract_caller()
    #get_storage_contract_caller()
    #get_storage_contract_public_data('data1')
    #get_secret_contract_caller()
    #getManage_DHKey_secret_contract('dataTest')
    getUser_DHKey_secret_contract('0x61bEa2058e8d5a01F1f9898E49F53Cc3cc8E6520', 'hello')
    #get_storage_contract_user_data('0x61bEa2058e8d5a01F1f9898E49F53Cc3cc8E6520', 'hello')
    #get_table_contract_dataStorageContractAddress()
    #get_table_contract_dataManageContractAddress()
    #get_table_contract_secretContractAddress()


