# 4. AES with Key Generation

## How to use

All input files must be located in the `res/` folder, while the output files are created in the `out/` folder.

## Execution

Each program that can be executed is listed here with its command line syntax and an example command.

### Encription (General)

```shell
python encrypt.py cbc <input_file:str> <key_file:str> <output_file:str> [input_vector_file:str]
```

### Decription (General)

```shell
python decrypt.py <operating_mode:str> <input_file:str> <key_file:str> <output_file:str> [input_vector_file:str]
```

### Encryption (CBC)

```shell
python encrypt.py cbc "Beispiel_Klartext.txt" "Beispiel_key.txt" "Beispiel_Klartext_cbc_encrypted.txt"
```

### Decryption (CBC)

```shell
python decrypt.py cbc "Beispiel_Kryptotext_cbc.txt" "Beispiel_key.txt" "Beispiel_Kryptotext_cbc_decrypted.txt"
```

### Encription (CTR)

```shell
python encrypt.py ctr "Beispiel_Klartext.txt" "Beispiel_key.txt" "Beispiel_Klartext_ctr_encrypted.txt"
```

### Decription (CTR)

```shell
python decrypt.py ctr "Beispiel_Kryptotext_ctr.txt" "Beispiel_key.txt" "Beispiel_Kryptotext_ctr_decrypted.txt"
```

### Encription (ECB)

```shell
python encrypt.py ecb "Beispiel_Klartext.txt" "Beispiel_key.txt" "Beispiel_Klartext_ecb_encrypted.txt"
```

### Decription (ECB)

```shell
python decrypt.py ecb "Beispiel_Kryptotext_ecb.txt" "Beispiel_key.txt" "Beispiel_Kryptotext_ecb_decrypted.txt"
```

### Encription (OFB)

```shell
python encrypt.py ofb "Beispiel_Klartext.txt" "Beispiel_key.txt" "Beispiel_Klartext_ofb_encrypted.txt" "Beispiel_Init_Vector.txt"
```

### Decription (OFB) !FUNKTIONIERT NOCH NICHT!

```shell
python decrypt.py ofb "Beispiel_Kryptotext_ofb.txt" "Beispiel_key.txt" "Beispiel_Kryptotext_ofb_decrypted.txt" "Beispiel_Init_vector.txt"
```
