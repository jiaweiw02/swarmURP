import json
from web3 import Web3, HTTPProvider

# dependencies
blockchainAddress = "HTTP://127.0.0.1:7545"
web3 = Web3(HTTPProvider(blockchainAddress))
compiledContractPath = "build/contracts/Auction.json"
deployedContractAddress = "0x993A4235E0042fCf3659B6bed516b36f83f8eCca"
with open(compiledContractPath) as file:
    contract_json = json.load(file)
    # contract abi is used to call the contract's functions
    contract_abi = contract_json['abi']

# reference deployed contract
contract = web3.eth.contract(address=deployedContractAddress, abi=contract_abi)

# function calls
