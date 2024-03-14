# 4. AES

## How to use

All input files must be located in the `res/` folder, while the output files are created in the `out/` folder.

## Execution

Each program that can be executed is listed here with its command line syntax and an example command.

### Encryption

```shell
python encrypt.py <input_file:str> <key_file:str> <output_file:str>
```

```shell
python encrypt.py "Beispiel_1_Klartext.txt" "Beispiel_key.txt" "Beispiel_1_Klartext_encrypted.txt"
```

### Decryption

```shell
python decrypt.py <input_file:str> <key_file:str> <output_file:str>
```

```shell
python decrypt.py "Beispiel_1_Kryptotext.txt" "Beispiel_key.txt" "Beispiel_1_Kryptotext_decrypted.txt"
```
