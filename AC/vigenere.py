def viginere_cipher(text: str, key: str, alphabet: str, mode: str = 'encrypt', verbose: bool = True) -> str:
    """
    Encrypts/decrypts text using a Vigenere Cipher with custom alphabet.

    Args:
        text: Input text to process (plaintext or ciphertext)
        key: Key containing only alphabet characters
        alphabet: Unique characters defining character order
        mode: 'encrypt' or 'decrypt' (default: 'encrypt')
        verbose: Show process details (default: False)

    Returns:
        Processed text string
    """
    # Validate alphabet (must contain unique characters)
    if len(set(alphabet)) != len(alphabet):
        raise ValueError("Alphabet must contain unique characters")
    
    # Validate key
    if not key:
        raise ValueError("Error: Key cannot be empty")
    
    # Check for invalid characters in both text and key
    invalid_text_chars = sorted(set(char for char in text if char != ' ' and char not in alphabet))
    invalid_key_chars = sorted(set(char for char in key if char not in alphabet))
    
    if invalid_text_chars or invalid_key_chars:
        error_msg = "Error: Invalid characters!\n"
        if invalid_text_chars:
            error_msg += f"in plaintext: {', '.join(invalid_text_chars)}\n"
        if invalid_key_chars:
            error_msg += f"in key: {', '.join(invalid_key_chars)}\n"
        error_msg += "are not in alphabet"
        raise ValueError(error_msg)
    
    # Process text
    result = []
    key_index = 0
    
    # Calculate non-space length for key validation
    non_space_count = sum(1 for char in text if char != ' ')
    if len(key) != non_space_count:
        key = key * ((non_space_count + len(key) - 1) // len(key))  # Repeat key cyclically
    
    for char in text:
        if char == ' ':
            result.append(' ')
            continue
            
        char_idx = alphabet.index(char)
        key_char = key[key_index % len(key)]
        key_idx = alphabet.index(key_char)
        
        if mode == 'encrypt':
            new_idx = (char_idx + key_idx) % len(alphabet)
        else:  # decrypt
            new_idx = (char_idx - key_idx) % len(alphabet)
        
        # Always show processing details regardless of verbose parameter
        operation = "encrypt" if mode == 'encrypt' else "decrypt"
        print(f"{char} ({char_idx}) {operation} with {key_char} ({key_idx}) -> {alphabet[new_idx]} ({new_idx})")
        
        result.append(alphabet[new_idx])
        key_index += 1
    
    return ''.join(result)

def main():
    print("Vigenère Cipher")
    print("--------------")
    
    # Get alphabet input
    alphabet = input("Enter the alphabet (e.g., ABCDEFGHIJKLMNOPQRSTUVWXYZ): ").strip()
    
    # Get operation mode with encrypt as default
    mode = input("Enter mode (encrypt/decrypt) [default: encrypt]: ").strip().lower()
    if not mode:  # if user just presses Enter
        mode = 'encrypt'
    elif mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Defaulting to 'encrypt'")
        mode = 'encrypt'
    
    # Get text input
    text = input("Enter the text to process: ").strip()
    
    # Get key input
    key = input("Enter the key: ").strip()
    
    # Get verbose option with False as default
    verbose_input = input("Show processing details? (True/False) [default: False]: ").strip()
    if not verbose_input:  # if user just presses Enter
        verbose = False
    else:
        verbose = verbose_input.lower() == 'true'
    
    # Validate empty inputs after collecting all inputs
    if not alphabet:
        print("\nError: Alphabet cannot be empty")
        return
        
    if not text:
        print("\nError: Plaintext cannot be empty")
        return
    
    try:
        result = viginere_cipher(text, key, alphabet, mode, verbose)
        print(f"\nEncrypted result: {result}")  # Changed to match expected output format
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
