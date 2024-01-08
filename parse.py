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
        # Find the end of the chunk
        end_index = min(start_index + chunk_size, len(transcript))

        # Adjust end_index to avoid splitting a word
        if end_index < len(transcript):
            while end_index > start_index and transcript[end_index] != ' ':
                end_index -= 1

        # Yield the chunk and update the start_index
        yield transcript[start_index:end_index]
        start_index = end_index + 1  # Skip the space

# Main script execution
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    transcript = get_youtube_transcript(video_url)

    if len(transcript) > 1000:
        print("Transcript is too long, sending in chunks...")
        for chunk in chunk_transcript(transcript):
            print(chunk)
            print("---- Next Chunk ----")
    else:
        print(transcript)
