import random
from PIL import Image
import os

def encrypt_image(image_path, key, output_path="encrypted.png"):
    """Encrypts an image using pixel manipulation and a secret key.

    Args:
        image_path (str): Path to the image file for encryption (absolute or relative path).
        key (int): Secret key used for encryption.
        output_path (str, optional): Path to save the encrypted image. Defaults to "encrypted.png".

    Returns:
        None
    """

    # Validate image path existence
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Open the image and access pixel data
    img = Image.open(image_path)
    pixels = img.load()

    # Validate key validity (e.g., ensure it's not 0 or too small)
    if not key:
        raise ValueError("Invalid key: Please provide a non-zero secret key.")

    # Encrypt each pixel using a combination of operations
    for i in range(img.width):
        for j in range(img.height):
            red, green, blue = pixels[i, j][:3]

            # Apply key-dependent shifts, swaps, or other operations (consider security-focused libraries)
            shifted_red = (red + key) % 256
            swapped_blue = blue
            blue = green
            green = swapped_blue

            pixels[i, j] = (shifted_red, green, blue)

    # Save the encrypted image
    img.save(output_path)

def decrypt_image(image_path, key, output_path="decrypted.png"):
    """Decrypts an image using the same key used for encryption.

    Args:
        image_path (str): Path to the encrypted image file.
        key (int): Secret key used for decryption (must match the encryption key).
        output_path (str, optional): Path to save the decrypted image. Defaults to "decrypted.png".

    Returns:
        None
    """

    # Validate image path existence
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {decrypt_path}")

    # Open the encrypted image and access pixel data
    img = Image.open(image_path)
    pixels = img.load()

    # Validate key validity (same as in encryption)

    # Decrypt each pixel using the inverse operations
    for i in range(img.width):
        for j in range(img.height):
            red, green, blue = pixels[i, j][:3]

            # Reverse shifts, swaps, or other operations
            shifted_red = (red - key) % 256
            swapped_blue = blue
            blue = green
            green = swapped_blue

            pixels[i, j] = (shifted_red, green, blue)

    # Save the decrypted image
    img.save(output_path)

if __name__ == "__main__":
    # Get user input for image paths and key, ensuring file existence
    while True:
        image_path = input("Enter image path (absolute or relative): ")
        if os.path.exists(image_path):
            break
        else:
            print("Invalid image path. Please enter a valid path.")

    key = int(input("Enter secret key: "))

    # Encrypt the image
    encrypt_image(image_path, key)

    # Decrypt the encrypted image using the same key
    decrypt_image("encrypted.png", key)
    print("Decryption complete!")