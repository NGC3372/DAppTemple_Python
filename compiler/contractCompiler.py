import os

storage_path = './contract/dataStorageContract.sol'
manage_path = './contract/dataManageContract.sol'
secret_path = './contract/secretKeyContract.sol'
table_path = './contract/tableContract.sol'

java_comp = 'epirus  generate solidity generate --abiFile=./{} --outputDir=./ --package=qwe'.format('abi_secret')
#os.system('solc {} --bin  --abi'.format(storage_path))
os.system(java_comp)
