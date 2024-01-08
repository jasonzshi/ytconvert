import sys
from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url):
    try:
        video_id = video_url.split('watch?v=')[1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([item['text'] for item in transcript_list])
        return transcript
    except Exception as e:
        return f"An error occurred: {e}"

def chunk_transcript(transcript, chunk_size=1000):
    start_index = 0
    end_index = 0

    while start_index < len(transcript):
        end_index = min(start_index + chunk_size, len(transcript))
        if end_index < len(transcript):
            while end_index > start_index and transcript[end_index] != ' ':
                end_index -= 1
        yield transcript[start_index:end_index].strip()
        start_index = end_index + 1

# Main script execution
if __name__ == "__main__":
    # Assuming YouTube URL is passed as a command-line argument
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        transcript = get_youtube_transcript(video_url)

        if len(transcript) > 1000:
            for chunk in chunk_transcript(transcript):
                print(chunk)
                print("---- Next Chunk ----")
        else:
            print(transcript)
    else:
        print("No YouTube URL provided")
