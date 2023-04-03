"""
Purpose:
    This program will take a video file and process it.
    pip install moviepy
"""

import os
import threading

from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx import speedx

# def load_clip(filename):
#     return VideoFileClip(filename)


# Set base directory path as a constant variable
BASE_DIR = r"C:\Users\Amma\Downloads\class_recordings"

# Set video filenames as constant variables
VIDEO_NAMES = [
    "1.mp4",
    "2.mp4",
    "3.mp4",
    # "4.mp4",
]

# Join base directory path with video filenames to get video paths
VIDEO_PATHS = [os.path.join(BASE_DIR, video) for video in VIDEO_NAMES]

# Method 1 - Sequential
videos_processed = [VideoFileClip(video) for video in VIDEO_PATHS]

# # Method 2  - using threading
# # Load each clip in a separate thread
# threads = []
# videos_processed = []
# for filename in VIDEO_PATHS:
#     thread = threading.Thread(target=lambda clip: videos_processed.append(load_clip(clip)), args=(filename,))
#     thread.start()
#     threads.append(thread)

# # Wait for all threads to finish
# for thread in threads:
#     thread.join()

# Merge videos with concatenate_videoclips()
final_video = concatenate_videoclips(videos_processed)

# Increase the play speed by a factor of 2
# final_video = speedx(final_video, factor=1.2)

final_video.write_videofile(os.path.join(BASE_DIR, "class38_pandas_series.mp4"))
