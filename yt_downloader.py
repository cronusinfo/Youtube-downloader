from pytube import YouTube

link = input("Enter link: ")
print("1. Download as MP4")
print("2. Download as MP3")
choice = input("Enter your choice (1 or 2): ")

print("Downloading...")

yt = YouTube(link)

if choice == '1':
    # Download as MP4 video
    video = yt.streams.filter(progressive=True).first()
    video.download()
    print("Video downloaded successfully!")
elif choice == '2':
    # Download as MP3 audio
    audio = yt.streams.filter(only_audio=True).first()
    audio.download()
    print("Audio downloaded successfully!")
else:
    print("Invalid choice.")

