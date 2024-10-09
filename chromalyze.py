import cv2
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def get_colors(path: str, samplerate: float = 0.03):
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        print(f"Error: Couldn't open video file {path}")
        exit()

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    skip = total_frames / (total_frames * samplerate)
    frame_number = 0
    bgrs = []
    with tqdm(total=total_frames, unit='frames') as pbar:
        while frame_number < total_frames:
            ret, frame = cap.read()
            if not ret:
                print("End of video or error reading frame.")
                break

            bgrs.append(frame.mean(axis=(0,1)))
            frame_number += skip
            pbar.update(skip)
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    cap.release()
    return np.array(bgrs)

def make_plot(bgrs: any, bins: int = 85):
    clrs = ['blue','green','red']

    bottom = np.zeros(bins)
    plt.hist(bgrs, bins, color=clrs, stacked=True)
    plt.title('histogram of average color of frame')
    plt.legend(clrs)
    plt.savefig('hist.png')

if __name__ == "__main__":
    import sys
    make_plot(get_colors(sys.argv[1]))
