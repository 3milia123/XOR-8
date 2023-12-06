def char_to_bin(char, bit_length=8):
    # Mengonversi karakter ke representasi biner dengan panjang tetap
    return format(ord(char), f'0{bit_length}b')

def xor_bits(bit1, bit2):
    # Operasi XOR antara dua bit
    return '1' if bit1 != bit2 else '0'

def equalize_length(message, key):
    # Menyamakan panjang pesan dan kunci dengan mengulang kunci jika lebih pendek
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    return key

def encrypt_bitwise(plaintext, key):
    # Enkripsi berbasis bit menggunakan XOR
    ciphertext_bits = [xor_bits(p, k) for p, k in zip(plaintext, key)]
    return ''.join(ciphertext_bits)

def decrypt_bitwise(ciphertext, key):
    # Dekripsi berbasis bit menggunakan XOR
    decrypted_bits = [xor_bits(c, k) for c, k in zip(ciphertext, key)]
    return ''.join(decrypted_bits)

def main():
    print("Enkripsi dan Dekripsi berbasis ASCII 8 BIT")
    print("Pilih")
    print("1. Enkripsi")
    print("2. Dekripsi")

    action = input("Pilih aksi (1/2): ")

    message = input("Masukkan pesan: ")
    key = input("Masukkan kunci (integer dan string / integer saja / string saja): ")

    # Menyamakan panjang pesan dan kunci
    key = equalize_length(message, key)

    # Konversi karakter ke bit
    message_bits = ''.join([char_to_bin(char, bit_length=8) for char in message])
    key_bits = ''.join([char_to_bin(char, bit_length=8) for char in key])

    print("\nBit pesan:")
    for i, char in enumerate(message):
        print(f"Karakter {char}: {message_bits[i*8:(i+1)*8]}")

    print("\nHasil XOR dari bit pesan dan bit kunci:")
    for i, char in enumerate(message):
        xor_result = xor_bits(message_bits[i*8:(i+1)*8], key_bits[i*8:(i+1)*8])
        print(f"{message_bits[i*8:(i+1)*8]} XOR {key_bits[i*8:(i+1)*8]} = {xor_result}")

    if action == '1':
        # Enkripsi
        encrypted_bits = encrypt_bitwise(message_bits, key_bits)

        # Output hanya karakter terenkripsi
        encrypted_message = ''.join([chr(int(encrypted_bits[i*8:(i+1)*8], 2)) for i in range(len(encrypted_bits)//8)])

        print("Hasil ada di hasil.txt")
        with open("hasil.txt", "w") as file:
            file.write("Encrypt Bit: " + encrypted_bits + "\n")
            file.write("Encrypt Message: " + encrypted_message)
    elif action == '2':
        # Dekripsi
        decrypted_bits = decrypt_bitwise(message_bits, key_bits)

        # Output hanya karakter terdekripsi
        decrypted_message = ''.join([chr(int(decrypted_bits[i*8:(i+1)*8], 2)) for i in range(len(decrypted_bits)//8)])

        print("Hasil ada di hasil.txt")
        with open("hasil.txt", "w") as file:
            file.write("Decrypt Bit: " + decrypted_bits + "\n")
            file.write("Decrypt Message: " + decrypted_message)
    else:
        print("Pilihan aksi tidak valid.")

if __name__ == "__main__":
    main()