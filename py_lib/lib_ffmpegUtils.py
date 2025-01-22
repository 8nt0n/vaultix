import subprocess
def get_video_length(filename):
    # Run the ffmpeg command to get information about the video file
    result = subprocess.run(['ffmpeg', '-i', filename], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    
    # Parse the output to find the duration
    output = result.stderr.decode()
    for line in output.splitlines():
        if "Duration" in line:
            duration = line.split()[1]
            return str(duration)[:-4]
    return -1