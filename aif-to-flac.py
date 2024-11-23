import os
import subprocess
import argparse

def batch_convert_aif_to_flac(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        return

    for file_name in os.listdir(directory):
        if file_name.lower().endswith('.aif'):
            input_file = os.path.join(directory, file_name)
            # Create the output FLAC file name by replacing the extension
            output_file = os.path.splitext(input_file)[0] + ".flac"
            try:
                # FFmpeg command AIF to FLAC
                subprocess.run([
                    'ffmpeg', 
                    '-i', input_file, 
                    output_file
                ], check=True)
                print(f"Converted: {file_name} to {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {file_name}: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert all AIF files in a directory to FLAC")
    # Add the directory argument
    parser.add_argument('directory', type=str, help="Path to the directory containing AIF files")
    # Parse the arguments
    args = parser.parse_args()
    batch_convert_aif_to_flac(args.directory)
