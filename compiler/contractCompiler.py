import os

storage_path = './contract/dataStorageContract.sol'
manage_path = './contract/dataManageContract.sol'
secret_path = './contract/secretKeyContract.sol'
table_path = './contract/tableContract.sol'

os.system('solc {} --bin  --abi'.format(storage_path))

