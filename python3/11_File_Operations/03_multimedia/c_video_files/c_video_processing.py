"""
Purpose:
    This program will take a video file and process it.
    pip install moviepy
"""

import os

from moviepy.editor import VideoFileClip, concatenate_videoclips

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


# Merge videos with concatenate_videoclips()
final_video = concatenate_videoclips(videos_processed)

# Increase the play speed by a factor of 2
# final_video = speedx(final_video, factor=1.2)

final_video.write_videofile(
    os.path.join(BASE_DIR, "class41_Exploratory_Data_Analysis_EDA.mp4")
)
