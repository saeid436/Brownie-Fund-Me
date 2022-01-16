import imp
from brownie import FundMe
from scripts.helpfulScripts import getAccount


def fund():
    fund_me = FundMe[-1]
    account = getAccount()
    entranceFee = fund_me.getEntranceFee()
    print(f'The current entery fee is {entranceFee}')
    print('Funding')
    fund_me.fund({'from':account, 'value':entranceFee})

def withdraw():
    funde_me = FundMe[-1]
    account = getAccount()
    funde_me.withdraw({'from':account})

def main():
    fund()
    withdraw()