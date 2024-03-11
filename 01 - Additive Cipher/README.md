# 01 Additive Cipher

## How to use

All input files must be located in the `res/` folder, while the output files are created in the `out/` folder.

## Execution

Each program that can be executed is listed here with its command line syntax and an example command.

### Encryption

```shell
python encrypt.py <input_file> <key> <output_file>
```

```shell
python encrypt.py "Klartext_1.txt" 3 "Klartext_1_encrypted.txt"
```

### Decryption

```shell
python decrypt.py <input_file> <key> <output_file>
```

```shell
python decrypt.py "Kryptotext_1_Key_7.txt" 7 "Kryptotext_1_Key_7_decrypted.txt"
```

### Auto Decryption

```shell
python auto_decrypt.py <input_file> <output_file>
```

```shell
python auto_decrypt.py "sampleEncrypted.txt" "sampleEncrypted_decrypted.txt"
```
