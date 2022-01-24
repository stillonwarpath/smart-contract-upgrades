from scripts.helpful_scripts import get_account, encode_function_data
from brownie import Box, ProxyAdmin, TransparentUpgradeableProxy


def test_proxy_upgrades():
    account = get_account()
    box = Box.deploy({"from": account})
    proxy_admin = ProxyAdmin.deploy({"from": account})
    box_encoded_initializer_function = encode_function_data()
    proxy = TransparentUpgradeableProxy.deploy(
        box.address, proxy_admin.address, box_encoded_initializer_function
    )
