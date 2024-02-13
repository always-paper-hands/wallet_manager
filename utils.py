import csv
from datetime import datetime
from eth_account import Account
from mnemonic import Mnemonic
from termcolor import colored
import sys
sys.__stdout__ = sys.stdout #solve error with inquirer import
from inquirer import prompt, List


class WalletCreate:
    @staticmethod
    def set_qty():
        while True:
            try:
                qty = int(input(colored('\nHow many accounts need to be created: ', 'light_cyan')))
                return qty
            except ValueError:
                print(colored("\nInvalid input. Enter a number.", 'red'))

    @staticmethod
    def set_amount():
        while True:
            try:
                amnt = int(input(colored('\nHow many "address-private key" pairs will be created under each seed phrase (Enter 1 by default): ', 'light_cyan')))
                return amnt
            except ValueError:
                print(colored("\nInvalid input. Enter a number.", 'red'))

    @staticmethod
    def set_seed_strength():
        strength_dict = {12: 128, 15: 160, 18: 192, 21: 224, 24: 256}
        while True:
            try:
                length = int(input(colored('\nHow many words would make up a seed phrase - 12/15/18/21/24: ','light_cyan')))
                if length in strength_dict:
                    return strength_dict[length]
                else:
                    print(colored("\nInvalid length of seed phrase. Please choose from the following options 12, 15, 18, 21 or 24.", 'red'))
            except ValueError:
                print(colored("\nInvalid input. Please enter a number.", 'red'))

    @staticmethod
    def determine_date_time():
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return now

    def create_evm_account(self):
        print(colored('\nThe accounts will be saved in a csv file in the following format "Seed-phrase | Address | Private Key"', 'light_cyan'))

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
              f'A total of {qty*amnt} wallets were created', 'green'))


class GetAddresses:

    @staticmethod
    def addr_from_pks():
        with open('data/pks.txt', 'r') as f:
            pks = [line.strip() for line in f]
            with open('result/addresses.txt', 'w') as f:
                for pk in pks:
                    if len(pk) < 64:
                        print(colored('Invalid private key', 'red'))
                    else:
                        address = Account.from_key(pk).address
                        f.write(address + '\n')
            print(colored('All valid addresses were successfully imported to result/addresses.txt', 'green'))


def choose_mode():
    questions = [
        List('prefered_path', message="Please choose one from the following options",
             choices=[
                'Create a batch of EVM accounts',
                'Get public addresses from private keys',
             ]
        )
    ]
    path = prompt(questions)['prefered_path']
    return ' '.join(path.split())
