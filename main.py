import os
import subprocess
import argparse

def resize_exr_images(input_folder, output_folder, size):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".exr"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            command = [
                "oiiotool",
                input_path,
                "--resize", size,
                "-o", output_path
            ]

            print(f"Resizing {filename} to {size}...")
            subprocess.run(command, check=True)

    print("✅ Done resizing all .exr files.")

def main():
    parser = argparse.ArgumentParser(description="Resize EXR images using oiiotool.")
    parser.add_argument("input_folder", help="Path to the input folder containing .exr files")
    parser.add_argument("output_folder", help="Path to save the resized .exr files")
    parser.add_argument("size", help="New size in format WIDTHxHEIGHT (e.g., 1024x1024)")

    args = parser.parse_args()

    resize_exr_images(args.input_folder, args.output_folder, args.size)

if __name__ == "__main__":
    main()