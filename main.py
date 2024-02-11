from utils import GetAddresses, WalletCreate, choose_mode
from termcolor import colored


def main():
    choice = choose_mode()
    if choice == 'Create a': #kostil
        WalletCreate().create_evm_account()
    else:
        GetAddresses().addr_from_pks()


if __name__ == '__main__':
    print(colored("""
 _   _   _   ______   _        _        ______ _______    _________   ______   ______   ______   ______   ______  ______  
| | | | | | | |  | | | |      | |      | |       | |     | | | | | \ | |  | | | |  \ \ | |  | | | | ____ | |     | |  | \ 
| | | | | | | |__| | | |   _  | |   _  | |----   | |     | | | | | | | |__| | | |  | | | |__| | | |  | | | |---- | |__| | 
|_|_|_|_|_/ |_|  |_| |_|__|_| |_|__|_| |_|____   |_|     |_| |_| |_| |_|  |_| |_|  |_| |_|  |_| |_|__|_| |_|____ |_|  \_\ \n """, 'red'))
    main()
    input(' > Press any button to close')
