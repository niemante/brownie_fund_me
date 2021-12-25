#  export NODE_OPTIONS=--openssl-legacy-provider
from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from":account}, 
        publish_source = config["networks"][network.show_active()].get("verify"),)
    print(f"contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()

# Deploying on ganache-cli was easy
# But on ganache it was hard: 
#   1) add network ganache local into "brownie network list"  
#   2) add ganache-local into config
#   3) LOCAL_BLOCKCHAIN_ENVIRONMENTS in helpfull
#   3) use it in helpfull AND in deploy

# Closing ganache would result in loosing all data... 
# and folder deployment would have useless info about what we did!
# DO NOT CLOSE
# Now we have deployed it. Interact with it is next:
# - create fund_and_withdraw.py