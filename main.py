from pytube import YouTube, Playlist

# print(yt.views)
# print(yt.title)
# print(yt.author)
# print(yt.length)
# print(yt.age_restricted)
# print(yt.publish_date)
# print(yt.description)

yt = YouTube('https://www.youtube.com/watch?v=BqhWfXh_Opg&list=WL&index=2')
# videos = yt.streams.filter(progressive=True)
# for video in videos:
#     print(video.resolution + "indiriliyor...")
#     video.download(filename=yt.title + "_" + video.resolution)


lst = Playlist("https://www.youtube.com/playlist?list=PLzMcBGfZo4-mYPQyPUciU_BkZHYXM42t6")
# for video in lst.videos:
#     print("indiriliyor" + video.title)
#     video.streams.first().download("twt")
