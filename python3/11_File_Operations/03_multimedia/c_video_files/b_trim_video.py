from moviepy.video.io.VideoFileClip import VideoFileClip


def trim_video(source_path, dest_path):
    # Load the video
    video = VideoFileClip(source_path)

    # Set the start and end time in seconds
    start_time = 42.2
    end_time = None

    # Cut the video
    cut_video = video.subclip(start_time, end_time)

    # Save the cut video to a file
    cut_video.write_videofile(dest_path)


trim_video("class31 WebServices Consuming REST API.mp4", "result.mp4")
