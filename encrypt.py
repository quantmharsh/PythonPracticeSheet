from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Generate a private and public key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Serialize the private key
private_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption())

# Serialize the public key
public_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

# Encrypt a message
message = b"123,laptop,4k display,59999,0x93e2471942D7F1bA873E7874caC7b548995B965D,0xB00f74c00f2498D8eb4e477C0B6A79618dB56EDA"
ciphertext = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

# Output the private and public keys, and the encrypted message
print("Private Key: ", private_pem.decode())
print("Public Key: ", public_pem.decode())
print("Encrypted message: ", ciphertext)

# Decrypt the message using the private key
plaintext = private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

print("Decrypted message: ", plaintext.decode())
