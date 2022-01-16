from brownie import accounts, network, exceptions
import pytest
from scripts.helpfulScripts import getAccount, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
import pytest

def test_can_fund_and_withdraw():
    account = getAccount()
    funde_me = deploy_fund_me()
    entranceFee = funde_me.getEntranceFee()+100
    tx = funde_me.fund({'from':account, 'value': entranceFee})
    tx.wait(1)
    assert funde_me.addressToAmountFunded(account.address) == entranceFee
    tx2 = funde_me.withdraw({'from':account})
    tx2.wait(1)
    assert funde_me.addressToAmountFunded(account.address) == 0

def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip('only for local testing!!')
    account = getAccount()
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({'from':bad_actor})