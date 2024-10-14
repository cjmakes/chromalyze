import cv2
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def bin_colors(path: str, samplerate: float = 0.03):
    cap = cv2.VideoCapture(path)
    bgr = np.zeros((3,256))

    if not cap.isOpened():
        print(f"Error: Couldn't open video file {path}")
        exit()

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    skip = total_frames / (total_frames * samplerate)
    frame_number = 0
    with tqdm(total=total_frames, unit='frames') as pbar:
        while frame_number < total_frames:
            ret, frame = cap.read()
            if not ret:
                print("End of video or error reading frame.")
                break

            for row in frame:
                for pixel in row:
                    bgr[0][pixel[0]]+=1
                    bgr[1][pixel[1]]+=1
                    bgr[2][pixel[2]]+=1

            frame_number += skip
            pbar.update(skip)
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    cap.release()
    return np.array(bgr)

def make_plot(bgrs: any, samplerate: float = 0.03):
    clrs = ['blue','green','red']

    bottom = np.zeros(256)
    for i in range(3):
        plt.bar(np.arange(256), bgrs[i], width=1.0, label=clrs[i], color=clrs[i], bottom=bottom)
    plt.title(f"histogram of pixel colors in a {samplerate} sample of frames")
    plt.yticks([])  
    plt.legend(clrs)
    plt.savefig('hist.png')

if __name__ == "__main__":
    import sys
    make_plot(bin_colors(sys.argv[1]))
