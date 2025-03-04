class BlockCipher:
    def __init__(self, key):
        # Validate key contains only ASCII printable characters
        for char in key:
            if not (32 <= ord(char) <= 126):
                raise ValueError("Error: Key must contain only ASCII printable characters")
                
        self.key = key
        self.block_size = 8  # fixed at 8 bytes
    
    def pad_message(self, message):
        """Pad the message with '_' to make it a multiple of block_size"""
        if len(self.key) != 8:
            raise ValueError("Error: Key must be exactly 8 characters")
        padding_needed = self.block_size - (len(message) % self.block_size)
        if padding_needed == self.block_size:
            return message
        return message + '_' * padding_needed
    
    def validate_message(self, message):
        """Validate message contains only ASCII printable characters"""
        for char in message:
            if not (32 <= ord(char) <= 126) and char != '_':
                raise ValueError("Error: Message must contain only ASCII printable characters")
    
    def encrypt(self, message):
        """Encrypt a message using ECB mode"""
        self.validate_message(message)
        padded_message = self.pad_message(message)
        
        result = []
        # Process each block
        for i in range(0, len(padded_message), self.block_size):
            block = padded_message[i:i+self.block_size]
            # XOR each character in the block with the corresponding character in the key
            for j in range(self.block_size):
                result.append(ord(block[j]) ^ ord(self.key[j]))
            
        return result
    
    def decrypt(self, encrypted_bytes):
        """Decrypt a message using ECB mode"""
        if len(encrypted_bytes) % self.block_size != 0:
            raise ValueError("Error: Encrypted data length must be a multiple of 8 bytes")
        
        decrypted = ""
        # Process each block independently (pure ECB mode)
        for i in range(0, len(encrypted_bytes), self.block_size):
            block = encrypted_bytes[i:i+self.block_size]
            # XOR each byte with corresponding byte in the key
            for j in range(self.block_size):
                decrypted += chr(block[j] ^ ord(self.key[j]))
        
        # Remove padding
        return decrypted.rstrip('_')
    
    def process(self, message, operation):
        """Process the message with the specified operation"""
        if operation.lower() not in ['encrypt', 'decrypt']:
            return "Error: Invalid operation. Use 'encrypt' or 'decrypt'"
        
        try:
            if operation.lower() == 'encrypt':
                result = self.encrypt(message)
                # Format as hex bytes separated by spaces
                return ' '.join(f"{byte:02X}" for byte in result)
            else:  # decrypt
                # Parse hex bytes
                bytes_to_decrypt = []
                for hex_byte in message.split():
                    bytes_to_decrypt.append(int(hex_byte, 16))
                return self.decrypt(bytes_to_decrypt)
        except ValueError as e:
            return str(e)


def main():
    # Get user inputs
    message = input("Enter message: ")
    key = input("Enter 8-character key: ")
    operation = input("Enter operation (encrypt/decrypt): ")
    
    try:
        cipher = BlockCipher(key)
        result = cipher.process(message, operation)
        print(result)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
