import os
import shutil
import random
import argparse


if __name__ == "__main__":

    # Usage
    # python split_dataset.py --data_path .\dataset\zootopia_enhanced_images256 --output_path .\dataset --split_size 250 500 1000 2500

    # Initialize parser
    parser = argparse.ArgumentParser(description='Extract frames from video.')

    # Adding arguments
    parser.add_argument('--split_size', nargs='+', type=int, required=True, help="Split size, can use multiple values")
    parser.add_argument('--data_path', type=str, required=True, help="The dataset path to split")
    parser.add_argument('--output_path', type=str, required=True, help="Output directory path")

    # Parsing arguments
    args = parser.parse_args()
    split_size = args.split_size
    data_path = args.data_path
    output_path = args.output_path

    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    for size in split_size:
        dest_path = os.path.join(output_path, os.path.basename(data_path) + f"_{size}")
        os.makedirs(dest_path)
        files = [
            shutil.copy(os.path.join(data_path, f), dest_path)\
            for f in random.sample(os.listdir(data_path), k=size)
        ]