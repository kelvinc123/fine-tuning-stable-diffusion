import os
import cv2
import argparse

# Initialize parser
parser = argparse.ArgumentParser(description='Extract frames from video.')

# Adding arguments
parser.add_argument('num_images', type=int, help='Number of images needed')
parser.add_argument('minutes_to_start', type=int, help='Minute to start frame extraction')
parser.add_argument('minutes_to_stop', type=int, help='Minute to stop frame extraction')
parser.add_argument('video_path', type=str, help='Path to the video file')
parser.add_argument('output_path', type=str, help='Path to save extracted images')

# Parsing arguments
args = parser.parse_args()


if __name__ == "__main__":

    # Params
    num_images = args.num_images
    minutes_to_start = args.minutes_to_start
    minutes_to_stop = args.minutes_to_stop
    video_path = args.video_path
    output_path = args.output_path

    # Create save directory if not available
    os.makedirs(output_path, exist_ok=True)

    # Start program
    cap = cv2.VideoCapture(video_path)

    # Define current frame and number of frame saved to calculate interval
    current_frame = 0
    current_frame_considered = 0
    num_frame_saved = 0

    # Calculate the frame
    seconds_to_start = minutes_to_start * 60
    seconds_to_stop = minutes_to_stop * 60
    frame_to_start = (round(cap.get(cv2.CAP_PROP_FPS)) * seconds_to_start) + 1
    frame_to_stop = (round(cap.get(cv2.CAP_PROP_FPS)) * seconds_to_stop) + 1
    intervals = (frame_to_stop - frame_to_start) // num_images

    while True:
        # Read a frame
        success, frame = cap.read()

        # If the frame was not successfully read, break the loop
        if not success:
            break

        
        current_frame += 1
        if current_frame < frame_to_start:
            continue
        elif current_frame > frame_to_stop:
            break

        # Save the frame at specified interval
        if current_frame_considered % intervals == 0:
            frame_name = f"frame_{num_frame_saved}.jpg"
            cv2.imwrite(os.path.join(output_path, frame_name), frame)
            num_frame_saved += 1

        current_frame_considered += 1
        print(f"Current frame: {current_frame}/{frame_to_stop}", end="\r")
        

    # Release the video capture object
    cap.release()

    # De-allocate any associated memory usage
    cv2.destroyAllWindows()