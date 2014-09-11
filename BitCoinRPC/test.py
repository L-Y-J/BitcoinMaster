# -*- coding:utf-8 -*-

from BitCoinRPC.bitcoinrpc.authproxy import AuthServiceProxy

access = AuthServiceProxy("http://user:123@127.0.0.1:9336")

"""
作用：返回当前状态信息
参数：
"""
# info = access.getinfo()
# difficulty = info['difficulty']
# blocks = info['blocks']
#
# print difficulty
# print blocks

# print access.listreceivedbyaddress(6)


"""
作用：返回当前难度
参数：
"""
# print access.getdifficulty()

"""
作用：返回账户明细
参数：钱包地址
"""
# print access.getaccount("LdVGdCbU8udRYneJU6HYdPU2zWPrVBGKEX")

"""
作用：返回钱包地址
参数：钱包用户名
"""
# print access.getaccountaddress("user")

"""
作用：返回钱包地址
参数：钱包用户名
"""





















