# 9. RSA Key Generation

## How to use

All input files must be located in the `res/` folder, while the output files are created in the `out/` folder.

## Execution

Each program that can be executed is listed here with its command line syntax and an example command.

### Key Generation

```shell
python generate_keys.py <length:int> <output_privat_key:str> <output_public_key:str> <output_primes:str>
```

```shell
python generate_keys.py 1000 "private_key.txt" "public_key.txt" "primes.txt"
```
