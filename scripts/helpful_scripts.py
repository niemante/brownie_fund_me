from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork","mainnet-fork-dev"]
DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS 
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])   

def deploy_mocks():
    # mock - created mock V3Agg
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS,STARTING_PRICE ,{"from": get_account()})
    print("Mocks Deployed!")  

# One way would be:
# brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork='https://mainnet.infura.io/v3/$WEB_INFURA_PROJECT_ID' accounts=10 mnemonic=brownie port=8545  
# or by Alchemy  (get key from Alchemy)
# brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/KY_eTgLFte_fZsENAFiVj5bNM1VtkTVh accounts=10 mnemonic=brownie port=8545  