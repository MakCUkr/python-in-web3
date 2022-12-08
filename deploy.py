import json
from web3 import Web3

provider_rpc = {
    "development": "https://goerli.infura.io/v3/3653806d884b401498e7a07f3f325d2e"
}
web3 = Web3(Web3.HTTPProvider(provider_rpc['development']))  # Change to correct network

account_from = {
    "private_key": "0x86a1457b21419627e2ec41bafd526ed11b0f685fdb0bba5efd605a63c2fb4c45",
    "address": "0x1Abf3a6C41035C1d2A3c74ec22405B54450f5e13",
}

print(f'Attempting to deploy from account: { account_from["address"] }')

abi = json.load(open("abi.json", "r"))
bytecode = "0x6100f561000f6000396100f56000f36003361161000c576100dd565b60003560e01c346100e35763a99e7e29811861008a57606436106100e35760043560040160648135116100e3578035806040526020820181816060375050506024358060a01c6100e35760e05260006040516060206020526000526040600020546100e35760e0516000604051606020602052600052604060002055005b63c3b2556d81186100db57604436106100e35760043560040160648135116100e357803580604052602082018181606037505050600060405160602060205260005260406000205460e052602060e0f35b505b60006000fd5b600080fda165767970657283000307000b"

Incrementer = web3.eth.contract(abi=abi, bytecode=bytecode)

construct_txn = Incrementer.constructor().buildTransaction(
    {
        'from': account_from['address'],
        'nonce': web3.eth.getTransactionCount(account_from['address']),
    }
)

tx_create = web3.eth.account.signTransaction(construct_txn, account_from['private_key'])
tx_hash = web3.eth.sendRawTransaction(tx_create.rawTransaction)
print(tx_hash.hex())
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print(f'Contract deployed at address: { tx_receipt.contractAddress }')