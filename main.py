from modules.wallet_create import WalletCreate
from modules.get_addresses import GetAddresses
from termcolor import colored


def main():
    print(colored('This program will help you with managing your EVM accounts.\n'
                                       'Please enter on of the following options:\n'
                                       '>>>1 - Create a batch of EVM accounts\n'
                                       '>>>2 - Get public addresses from private keys\n', 'light_cyan', 'on_black'))
    while True:
        try:
            option = int(input())
            if option == 1:
                WalletCreate().create_evm_account()
                break
            elif option == 2:
                GetAddresses().addr_from_pks()
                break
            # elif option == 3:
            #     GetAddresses().addr_from_mnemonic()
            #     break
            else:
                print(colored("\nInvalid number. Enter a number from the list.\n", 'red', 'on_black'))
        except ValueError:
            print(colored("\nInvalid input. Enter a number.\n", 'red', 'on_black'))


if __name__ == '__main__':
    print(colored("""
                                                                                                                                                                 
 **       **     **     **       **       ******** **********              ****     ****     **     ****     **     **       ********  ******** *******  
/**      /**    ****   /**      /**      /**///// /////**///              /**/**   **/**    ****   /**/**   /**    ****     **//////**/**///// /**////** 
/**   *  /**   **//**  /**      /**      /**          /**                 /**//** ** /**   **//**  /**//**  /**   **//**   **      // /**      /**   /** 
/**  *** /**  **  //** /**      /**      /*******     /**                 /** //***  /**  **  //** /** //** /**  **  //** /**         /******* /*******  
/** **/**/** **********/**      /**      /**////      /**                 /**  //*   /** **********/**  //**/** **********/**    *****/**////  /**///**  
/**** //****/**//////**/**      /**      /**          /**                 /**   /    /**/**//////**/**   //****/**//////**//**  ////**/**      /**  //** 
/**/   ///**/**     /**/********/********/********    /**                 /**        /**/**     /**/**    //***/**     /** //******** /********/**   //**
//       // //      // //////// //////// ////////     //                  //         // //      // //      /// //      //   ////////  //////// //     //   \n                                                                                                                                                            
""", 'red', 'on_black', ['bold']))

    main()
