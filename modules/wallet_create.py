import csv
from datetime import datetime
from eth_account import Account
from mnemonic import Mnemonic
from termcolor import colored


class WalletCreate:
    @staticmethod
    def set_qty():
        while True:
            try:
                qty = int(input(colored('\nHow many accounts need to be created: ', 'light_cyan', 'on_black')))
                return qty
            except ValueError:
                print(colored("\nInvalid input. Enter a number.", 'red', 'on_black'))

    @staticmethod
    def set_amount():
        while True:
            try:
                amnt = int(input(colored('\nHow many "address-private key" pairs will be created under each seed phrase (Enter 1 by default): ', 'light_cyan', 'on_black')))
                return amnt
            except ValueError:
                print(colored("\nInvalid input. Enter a number.", 'red', 'on_black'))

    @staticmethod
    def set_seed_strength():
        strength_dict = {12: 128, 15: 160, 18: 192, 21: 224, 24: 256}
        while True:
            try:
                length = int(input(colored('\nHow many words would make up a seed phrase - 12/15/18/21/24: ','light_cyan', 'on_black')))
                if length in strength_dict:
                    return strength_dict[length]
                else:
                    print(colored("\nInvalid length of seed phrase. Please choose from the following options 12, 15, 18, 21 or 24.", 'red', 'on_black'))
            except ValueError:
                print(colored("\nInvalid input. Please enter a number.", 'red', 'on_black'))

    @staticmethod
    def determine_date_time():
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return now

    def create_evm_account(self):
        print(colored('\nThe accounts will be saved in a csv file in the following format "Seed-phrase | Address | Private Key"', 'light_cyan', 'on_black', ['bold']))

        qty = self.set_qty()
        amnt = self.set_amount()
        now = self.determine_date_time()
        title = [
            [f'-/-/-/-/-/-/-/-', f'{now}', '-/-/-/-/-/-/-/-'],
            ['Seed-pharse', 'Address', 'Private Key']
        ]

        with open('result/accounts.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(title)
        Account.enable_unaudited_hdwallet_features()
        strength = self.set_seed_strength()

        for i in range(qty):
            mnemo = Mnemonic("english")
            mnemonic = mnemo.generate(strength=strength)

            for j in range(amnt):
                account = Account.from_mnemonic(
                    mnemonic=mnemonic,
                    account_path=f"m/44'/60'/0'/0/{j}"
                )
                if j == 0:
                    row = [mnemonic, account.address, account.key.hex()]
                else:
                    row = ['', account.address, account.key.hex()]

                with open('result/accounts.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(row)

        print(colored(f'\n{qty} seed-phrases with {amnt} "address-private key" pairs were created\n'
              f'A total of {qty*amnt} wallets were created', 'light_cyan', 'on_black'))
