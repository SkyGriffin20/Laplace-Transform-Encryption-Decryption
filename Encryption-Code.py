def encrypt_string(input_string, r):
    numerical_values = [ord(char) - ord('a') + 1  for char in input_string.lower()]

    q_values = []
    # Compute the coefficients (q values) directly from the numerical values
    for i, value in enumerate(numerical_values):
        # Using the formula directly
        # We take only the coefficient part, G_i * (2i+1) * (r^2i)
        if value != 0:
            q = int(value * r**(2*i) * (2 * i + 1))
        else:
            q = 0
        q_values.append(q)

    quotients = [int(q/26) for q in q_values]
    encrypted_chars = [chr((q % 26) + ord('a') - 1).upper() for q in q_values]

    print("Keys: ")
    print(quotients)
    return ''.join(encrypted_chars)

input = 'SKYGRIFFIN'
print('Input: ', input)
print("Encrypted Text: ",encrypt_string(input,2))