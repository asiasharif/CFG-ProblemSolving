import string

alphabet = string.ascii_lowercase  # built in function for string gives you all the alphabets
key = 2
word = input('please enter a word')

def ceaser_cipher():
    encrypted_message = ''
    for i in word:
        if i in alphabet:
            encrypted_message += (alphabet[(alphabet.index(i) + key) % 26])
        else:
            encrypted_message += ' '
    return encrypted_message


print(ceaser_cipher())

# index_i = alphabet.index(i)
# print(index_i)
# add_key = index_i + key
# print(add_key)
# modulo = add_key % 26
# print(modulo)



# modulus for remainder - is used to wrap round the alphabet to get 'z' to become 'a'
