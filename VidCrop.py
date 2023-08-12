from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def process_video(input_path, output_path):
    # Load the video clip
    video_clip = VideoFileClip(input_path)
    
    # Delete the first 30 seconds
    trimmed_clip = video_clip.subclip(30, None)
    
    # Save the next 29 seconds
    final_clip = trimmed_clip.subclip(0, 29)
    final_clip.write_videofile(output_path, codec="libx264")
    
    # Close the video clips
    video_clip.close()
    trimmed_clip.close()
    final_clip.close()

# Specify input and output file paths
input_video_path = r'C:\Setup_code\xs.mp4'
output_video_path = r'C:\Setup_code\unique_screenshots\output_video.mp4'

# Process the video
process_video(input_video_path, output_video_path)

# Install ImageMagick: ImageMagick is a powerful image manipulation tool. You can download and install it from their official website: https://imagemagick.org/script/download.php

# Make sure to add the convert command to your system's PATH during installation.

# Install FFmpeg: FFmpeg is a multimedia framework that includes a set of tools for processing audio and video. You can download a build of FFmpeg from their official website: https://www.ffmpeg.org/download.html

# Add the directory containing the ffmpeg executable to your system's PATH.