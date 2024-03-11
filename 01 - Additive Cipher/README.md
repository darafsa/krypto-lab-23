# How to use

## Important Note

input_files need to be stored in "./res/", output_files will always be generated in "./out/"

## Encryption

```shell
python encrypt.py <input_file> <key> <output_file>
```

Example:

```shell
python encrypt.py "Klartext_1.txt" 3 "Klartext_1_encrypted.txt"
```

## Decryption

```shell
python decrypt.py <input_file> <key> <output_file>
```

Example:

```shell
python decrypt.py "Kryptotext_1_Key_7.txt" 7 "Kryptotext_1_Key_7_decrypted.txt"
```

## Auto Decryption

```shell
python auto_decrypt.py <input_file> <output_file>
```

Example:

```shell
python auto_decrypt.py "sampleEncrypted.txt" "sampleEncrypted_decrypted.txt"
```
