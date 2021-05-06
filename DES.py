#Author Komeyl Kalbali komeyl.kalbali.dev@gmail.com

from DESCommon import DES, generate_keys
from DESUtil import to_binary, add_pads_if_necessary, hex_to_bin, bin_to_hex, bin_to_text

try:
    input = raw_input
except NameError:
    pass

def get_bits(plaintext):
    text_bits = []
    for i in plaintext:
        text_bits.extend(to_binary(ord(i)))
    return text_bits

def encrypt(plaintext, key_text):
	keys = generate_keys(key_text)

	text_bits = get_bits(plaintext)
	text_bits = add_pads_if_necessary(text_bits)

	final_cipher = ''
	for i in range(0, len(text_bits), 64):
		final_cipher += DES(text_bits, i, (i+64), keys)

	# conversion of binary cipher into hex-decimal form
	hex_cipher = ''
	i = 0
	while i < len(final_cipher):
		hex_cipher += bin_to_hex(final_cipher[i:i+4])
		i = i+4
	return hex_cipher

def main():

    key_text = str(input('Hi sir Enter the key\n'))

    if(len(key_text) < 8):
    	print('Key must be 8 characters in length. Exiting...')
    	return

    if(1):
        plaintext = str(input('Enter the message(in Text-form)\n'))
        cipher = encrypt(plaintext, key_text)
        print('the cipher is(in hex-decimal form)')
        print(cipher)

    print('exiting...')
    return

if __name__ == "__main__":
    main()
