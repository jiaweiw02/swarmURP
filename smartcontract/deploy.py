import json
from web3 import Web3, HTTPProvider

blockchainAddress = "HTTP://127.0.0.1:7545"

web3 = Web3(HTTPProvider(blockchainAddress))

# 0xD7108e07B0312EE1FDA2ff8bE873860Fee022cfa
web3.eth.defaultAccount = web3.eth.account[1]

compiledContractPath = "build/contracts/Auction.json"

deployedContractAddress = "0x4D8dc1D7328E62bEECBF8F953134331Aa0152796"

with open(compiledContractPath) as file:
    contract_json = json.load(file)

    # fetch contract's abi - necessary to call its functions
    contract_abi = contract_json['abi']

# Fetching deployed contract reference
contract = web3.eth.contract(
    address=deployedContractAddress, abi=contract_abi)

# Calling contract function (this is not persisted
# to the blockchain)
output = contract.functions.hello().call()

print(output)
