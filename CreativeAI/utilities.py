from enum import Enum
from pathlib import Path
from typing import Union

import cv2
import numpy as np


class CocoPart(Enum):
    Nose = 0
    Neck = 1
    RShoulder = 2
    RElbow = 3
    RWrist = 4
    LShoulder = 5
    LElbow = 6
    LWrist = 7
    RHip = 8
    RKnee = 9
    RAnkle = 10
    LHip = 11
    LKnee = 12
    LAnkle = 13
    REye = 14
    LEye = 15
    REar = 16
    LEar = 17
    Background = 18


CocoSmall = [CocoPart.Nose.value, CocoPart.Neck.value, CocoPart.RShoulder.value,
             CocoPart.RElbow.value, CocoPart.RWrist.value, CocoPart.LShoulder.value,
             CocoPart.LElbow.value, CocoPart.LWrist.value, CocoPart.RHip.value,
             CocoPart.RKnee.value, CocoPart.RAnkle.value, CocoPart.LHip.value,
             CocoPart.LKnee.value, CocoPart.LAnkle.value]

CocoPairs = [
    (1, 2), (1, 5), (2, 3), (3, 4), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (1, 11),
    (11, 12), (12, 13), (1, 0), (0, 14), (14, 16), (0, 15), (15, 17), (2, 16), (5, 17)
]
CocoPairsRender = CocoPairs[:-2]

CocoColors = [[255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0],
              [0, 255, 85], [0, 255, 170], [0, 255, 255], [0, 170, 255], [0, 85, 255], [0, 0, 255], [85, 0, 255],
              [170, 0, 255], [255, 0, 255], [255, 0, 170], [255, 0, 85]]


def draw_humans(img, data, skeleton_only=False):
    if skeleton_only:
        img = np.ones(img.shape)

    image_h, image_w = img.shape[:2]
    for i, row in data.iterrows():
        centers = {}

        for part_idx, x, y in zip(row["part_idx"], row["x"], row["y"]):
            center = (int(x * image_w + 0.5), int(y * image_h + 0.5))
            centers[int(part_idx)] = center
            cv2.circle(img, center, 3, CocoColors[int(part_idx)], thickness=3,
                       lineType=8, shift=0)

            # draw line
        for pair_order, pair in enumerate(CocoPairsRender):
            if pair[0] not in centers or pair[1] not in centers:
                continue
            cv2.line(img, centers[pair[0]], centers[pair[1]], CocoColors[pair_order], 3)

    return img


def draw_humans_video(video, poses, skeleton_only=False):
    video_poses = np.array(
        [draw_humans(video[int(frame)].copy(), poses[poses.frame == frame], skeleton_only=skeleton_only) for frame in
         range(len(video))])
    return video_poses


def load_video(video_path: Union[str, Path], fps: int = -1, width=-1, height=-1):
    from decord import VideoReader, cpu

    reader = VideoReader(str(video_path), ctx=cpu(0), width=width, height=height)
    frames_to_skip = 1
    if fps > 0:
        video_fps = reader.get_avg_fps()
        fps = min(fps, video_fps)
        frames_to_skip = int(video_fps / fps)
        if frames_to_skip == 0:
            return None

    indices = list(range(0, len(reader), frames_to_skip))
    frames = reader.get_batch(indices).asnumpy()
    return frames


def save_video_old(video, path: Union[Path, str], fps=10):
    size = (video.shape[2], video.shape[1])
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(str(path), fourcc, fps, size)
    for frame in video:
        out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    out.release()


def save_video(video, path: Union[Path, str], fps=10):
    import imageio
    writer = imageio.get_writer(str(path), fps=fps)
    for frame in video:
        writer.append_data(frame)
    writer.close()


def save_video_with_sound(video, video_path, result_path: Path, fps):
    import ffmpeg
    temp_path = result_path.parent / "temp.mp4"
    save_video(video, temp_path, fps=fps)
    temp_ffmpeg_path = ffmpeg.input(str(temp_path))
    sound_path = ffmpeg.input(str(video_path))
    try:
        ffmpeg.concat(temp_ffmpeg_path, sound_path, v=1, a=1).output(str(result_path)).run(
            capture_stdout=True, capture_stderr=True)
    except ffmpeg.Error as e:
        print("Error", e)
        print('stdout:', e.stdout.decode('utf8'))
        print('stderr:', e.stderr.decode('utf8'))
        raise e
    temp_path.unlink()
