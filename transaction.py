from web3 import Web3

provider_rpc = {
    "development": "https://goerli.infura.io/v3/3653806d884b401498e7a07f3f325d2e"
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["development"]))  # Change to correct network

account_from = {
    "private_key": "0x86a1457b21419627e2ec41bafd526ed11b0f685fdb0bba5efd605a63c2fb4c45",
    "address": "0x1Abf3a6C41035C1d2A3c74ec22405B54450f5e13",
}
address_to = "0x5aDF576358c64d33C61378876cbfA342aff9a5D4"

print(
    f'Attempting to send transaction from { account_from["address"] } to { address_to }'
)

tx_create = web3.eth.account.signTransaction(
    {
        "nonce": web3.eth.getTransactionCount(account_from["address"]),
        "gasPrice": 20000000000,
        "gas": 1000000,
        "to": address_to,
        "value": web3.toWei("0.2", "ether"),
    },
    account_from["private_key"],
)

print("Signed")
tx_hash = web3.eth.sendRawTransaction(tx_create.rawTransaction)
print(tx_hash.hex())
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print(f"Transaction successful with hash: { tx_receipt.transactionHash.hex() }")