def decrypt_string(encrypted_string, k_values,r):
    G_dash_values = [ord(char) - ord('A') + 1 for char in encrypted_string]
    q_values = [26 * k + G_prime for k, G_prime in zip(k_values, G_dash_values)]
    G_values = []

    #Reverse-Engineering Gi values
    for i, value in enumerate(q_values):
        if value != 0:
            g = int(value/(((2*i)+1)(r*(2*i))))
        else:
            g = 0

        G_values.append(g)
    original_string = ''.join(chr(q % 26 + ord('a') - 1).upper() for q in G_values)

    return original_string

print("Decrypted Text: ")
decrypt_string('SBXPBB`VDT', [0, 5, 76, 120, 1595, 3899, 12288, 56713, 385654,2681934],2)