from pytube import YouTube

def download_audio(link):
    try:
        youtube_object = YouTube(link)
        download_location = input("Enter the download location (folder path): ")  # D:\music
        audio_stream = youtube_object.streams.filter(only_audio=True).get_highest_resolution()
        audio_stream.download(download_location)
        print("Audio download is completed successfully.")
    except Exception as e:
        print("An error has occurred:", str(e))

link = input("Enter the YouTube video URL: ")
download_audio(link)
