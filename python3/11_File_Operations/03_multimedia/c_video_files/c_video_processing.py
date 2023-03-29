# # install moviepy via pip
# # pip install moviepy

# # We can import some python libraries before starting to merge videos.
# from moviepy.editor import VideoFileClip, concatenate_videoclips
# from moviepy.video.fx import speedx
# import threading

# def load_clip(filename):
#     return VideoFileClip(filename)


# videos = [
#     r"C:\Users\Amma\Downloads\class_recordings\video1051222424.mp4",
#     r"C:\Users\Amma\Downloads\class_recordings\video1107962880.mp4",
#     # r"C:\Users\Amma\Downloads\class_recordings\3.mp4",
#     # r'C:\Users\Amma\Downloads\class_recordings\4.mp4',
# ]

# # Method 1 - Sequential
# videos_processed = [VideoFileClip(video) for video in videos]

# # # Method 2  - using threading
# # # Load each clip in a separate thread
# # threads = []
# # videos_processed = []
# # for filename in videos:
# #     thread = threading.Thread(target=lambda clip: videos_processed.append(load_clip(clip)), args=(filename,))
# #     thread.start()
# #     threads.append(thread)

# # # Wait for all threads to finish
# # for thread in threads:
# #     thread.join()

# # Merge videos with concatenate_videoclips()
# final_video = concatenate_videoclips(videos_processed)

# # Increase the play speed by a factor of 2
# # final_video = speedx(final_video, factor=1.2)

# final_video.write_videofile(
#     r"C:\Users\Amma\Downloads\class_recordings\class34_Flask_web_applications.mp4"
# )


# # from string import *

# # method = "METHODS"

# # def x(methods):
# #     method = str.swapcase(methods)
# #     print("%(method)s" % locals())

# # methods = str.swapcase(method[:-1])
# # x(methods)


class I:
    num = 0

    def __init__(self) -> None:
        self.num = 0

    def method(self):
        return

    def methodA(self):
        I.num = 0

    def methodB(self):
        I.num += 1

    def methodC(self):
        self.num += 1

    def methodD(cls):
        I.num = I.num + 1

    methodD = classmethod(methodD)

    def methodE(cls):
        return I.num

    methodE = classmethod(methodE)

    def methodF():
        return I.num

    methodF = staticmethod(methodF)

    def methodG(self):
        self.num = self.num + 1

    def methodH(self):
        self.num = I.num
        return self.num


print(f"{I.methodE() =}")

K = I()

print(f"{K.methodG() = }")
print(f"{K.methodE() = }")

# print(f'{I.methodB() =}')
# print(f'{I.methodH() =}')
print(f"{I.methodF() =}")

# # for n in range(2, 10):
# #     for x in range(2, n):
# #         if n % x == 0:
# #             break
# #     else:
# #         print(n)
