from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
link = "https://youtu.be/exMx3_SzUYs"
Download(link)
