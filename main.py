import sys
from config import num_words
from web3.auto import w3


def wallets_creation(num):
    addresses = []
    private_keys = []
    mnemonics = []
    w3.eth.account.enable_unaudited_hdwallet_features()
    for i in range(num):
        new_account = w3.eth.account.create_with_mnemonic(num_words=num_words)
        addresses.append(new_account[0].address)
        private_keys.append(new_account[0]._private_key.hex())
        mnemonics.append(new_account[1])

        print("New address:", addresses[-1])

    return addresses, private_keys, mnemonics


def main():
    w_number = int(input("How many wallets create? "))
    addresses, private_keys, mnemonics = wallets_creation(w_number)

    with open("wallet.txt", "w") as f:
        for i in range(len(addresses)):
            f.write(f'{str(addresses[i])},{str(private_keys[i])},{str(mnemonics[i])}\n')
    # Сохранение сид-фразы в файл
    with open('mnemonic.txt', 'w') as f:
        for i in range(len(mnemonics)):
            f.write(f'{str(mnemonics[i])}\n')
    # Сохранение приватного ключа в файл
    with open('private_key.txt', 'w') as f:
        for i in range(len(private_keys)):
            f.write(f'{str(private_keys[i])}\n')
    # Сохранение адреса
    with open('address.txt', 'w') as f:
        for i in range(len(addresses)):
            f.write(f'{str(addresses[i])}\n')
    print("Сид-фразы сохранены в файле mnemonic.txt")
    print("Приватные ключи сохранены в файле private_key.txt")
    print("Адреса сохранены в файле address.txt")
    print("Seed+private+public сохранены в файле wallet.txt")


if __name__ == '__main__':
    main()
