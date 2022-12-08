from web3 import Web3

provider_rpc = {
    "development": "https://goerli.infura.io/v3/3653806d884b401498e7a07f3f325d2e"
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["development"]))  # Change to correct network

address_from = "0x1Abf3a6C41035C1d2A3c74ec22405B54450f5e13"
address_to = "0x5aDF576358c64d33C61378876cbfA342aff9a5D4"

balance_from = web3.fromWei(web3.eth.getBalance(address_from), "ether")
balance_to = web3.fromWei(web3.eth.getBalance(address_to), "ether")

print(f"The balance of { address_from } is: { balance_from } ETH")
print(f"The balance of { address_to } is: { balance_to } ETH")