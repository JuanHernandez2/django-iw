from string import ascii_uppercase

def num_to_col_letters(num, alphabet):
    letters = ''
    if num <= 27:
        return alphabet[num-1]
    else:
        while num:
            mod = (num-1) % len(alphabet)
            letters += alphabet[mod]
            num = (num - 1) // len(alphabet)
        return ''.join(reversed(letters))

if __name__ == "__main__":
    alphabet = list(ascii_uppercase)
    alphabet.insert(14, 'Ñ')
    num = int(input("Ingrese el numero: "))
    msg = f'Num = {num}   Column = {num_to_col_letters(num, alphabet)}'
    print(msg)
    
    

