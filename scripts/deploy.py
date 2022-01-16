import imp
from brownie import accounts, FundMe, MockV3Aggregator, network, config
from scripts.helpfulScripts import deployMocks, getAccount, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    
    account = getAccount()
    
    # if we are on persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        priceFeedAddress = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deployMocks()
        priceFeedAddress = MockV3Aggregator[-1].address
    
    fundMe = FundMe.deploy(
    priceFeedAddress,
    {'from':account},
     publish_source= config['networks'][network.show_active()].get('verify'),
     )
    
    print(f'Contract Deployed to {fundMe.address}')
    #return fundMe


def main():
    deploy_fund_me()