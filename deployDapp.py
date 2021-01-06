from myWeb3 import myWeb3

abi_list = {'manage': 'compiler/abi_manage',
            'storage': 'compiler/abi_storage',
            'table': 'compiler/abi_table',
            'secret': 'compiler/abi_secret'}
bytecode_list = {'manage': 'compiler/bytecode_manage',
                 'storage': 'compiler/bytecode_storage',
                 'table': 'compiler/bytecode_table',
                 'secret': 'compiler/bytecode_secret'}


def deploy_contract(file_name, private_key):
    w3 = myWeb3()
    w3.initAccount(privateKey=private_key)
    abi = abi_list[file_name]
    bytecode = bytecode_list[file_name]
    abi_file = open(abi, 'r')
    abi = abi_file.read()
    abi_file.close()
    bytecode_file = open(bytecode, 'r')
    bytecode = bytecode_file.read()
    bytecode_file.close()
    contract = w3.createContract(byteCode=bytecode, ABI=abi)
    result = w3.deployContract(contract)
    print(result)


deploy_contract('secret', 'dda1ec2a2312151ac7d82cb9842b72c93edcad903b44a185387cd53fd2c29625')
