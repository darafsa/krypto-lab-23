# 2. Vigenere Cipher

## How to use

All input files must be located in the `res/` folder, while the output files are created in the `out/` folder.

## Execution

Each program that can be executed is listed here with its command line syntax and an example command.

### Encryption

```shell
python encrypt.py <input_file:str> <key:str> <output_file:str>
```

```shell
python encrypt.py "Klartext_1.txt" "TAG" "Klartext_1_encrypted.txt"
```

### Decryption

```shell
python decrypt.py <input_file:str> <key:str> <output_file:str>
```

```shell
python decrypt.py "Kryptotext_TAG.txt" "TAG" "Kryptotext_TAG_decrypted.txt"
```

### Auto Decryption

```shell
python auto_decrypt.py <input_file:str> <output_file:str>
```

```shell
python auto_decrypt.py "Kryptotext_TAG.txt" "Kryptotext_TAG_auto_decrypted.txt"
```
