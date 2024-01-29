from eth_account import Account
from modules.wallet_create import WalletCreate


class GetAddresses:

    @staticmethod
    def addr_from_pks():
        try:
            with open('data/pks.txt', 'r') as f:
                pks = [line.strip() for line in f]
                if len(pks) == 0:
                    raise ValueError('Fill pks.txt', 'red', 'on_black')
                else:
                    with open('result/addresses.txt', 'w') as f:
                        for pk in pks:
                            address = Account.from_key(pk).address
                            f.write(address + '\n')
                    print('Addresses were successfully imported to result/addresses.txt', 'light_cyan', 'on_black')
        except Exception as e:
            print()


    # @staticmethod
    # def addr_from_mnemonic():
    #     amnt = WalletCreate.set_amount()
    #     with open('data/mnemonics.txt', 'r') as f:
    #         seeds = [line.strip() for line in f]
    #     with open('result/addresses.txt', 'w') as f:
    #         for seed in seeds:
    #             for j in amnt:
    #                 address = Account.from_mnemonic(mnemonic=seed, account_path=f"m/44'/60'/0'/0/{j}").address
    #                 f.write(address + '\n')
