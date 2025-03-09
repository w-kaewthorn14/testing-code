def caesarCipher(s, k):
    result = []
    k = k % 26  # Ensure k is within the range of the alphabet
    
    for char in s:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            new_char = chr(shift + (ord(char) - shift + k) % 26)
        else:
            new_char = char
        
        result.append(new_char)
    
    return ''.join(result)

if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    
    print(caesarCipher(s, k))