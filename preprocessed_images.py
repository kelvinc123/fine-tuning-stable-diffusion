import os
import cv2
import argparse
from PIL import Image
from tqdm import tqdm

# Initialize parser
parser = argparse.ArgumentParser(description='Extract frames from video.')

# Adding arguments
parser.add_argument('data_path', type=str, help='Directory containing images')
parser.add_argument('output_path', type=str, help='Path to save preprocessed images')
parser.add_argument('output_size', type=int, help='Heigth and Width for output')
parser.add_argument('--only_one', action='store_true', help='Preprocessed only one sample for testing')

# Parsing arguments
args = parser.parse_args()

if __name__ == "__main__":

    # Params
    data_path = args.data_path
    output_path = args.output_path
    output_size = args.output_size
    only_one = args.only_one

    # Create save directory if not available
    os.makedirs(output_path, exist_ok=True)

    # Get the filenames from data_path
    files = os.listdir(data_path)

    for i in tqdm(range(len(files))):
        image = cv2.imread(os.path.join(data_path, files[i]))

        original_height, original_width = image.shape[:2]
        desired_size = min([original_height, original_width])

        start_x = (original_width - desired_size) // 2
        end_x = start_x + desired_size

        start_y = (original_height - desired_size) // 2
        end_y = start_y + desired_size

        # Crop the image
        cropped_image = image[start_y:end_y, start_x:end_x]

        # Resize the image
        resized_image = cv2.resize(
            cropped_image, (output_size, output_size), interpolation=cv2.INTER_AREA
        )

        # Save the cropped image
        cv2.imwrite(os.path.join(output_path, files[i]), resized_image)

        # If only_one, don't continue and stops here. 
        if only_one:
            break

    # De-allocate any associated memory usage
    cv2.destroyAllWindows()