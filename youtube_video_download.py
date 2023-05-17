from pytube import YouTube


def Download(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()

    download_location = input("Enter the download location (folder path): ") # D:\music

    try:
        youtube_object.download(download_location)
        print("Download is completed successfully")
    except:
        print("An error has occurred")


link = input("Enter the YouTube video URL: ")
Download(link)
