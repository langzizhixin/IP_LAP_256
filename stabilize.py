# 后处理：使用 OpenCV 进行视频稳定
import cv2
import numpy as np

cap = cv2.VideoCapture("./test_result/555result_N_25_Nl_25.mp4")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./test_result/stable_output_video.mp4', fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 在这里应用视频稳定算法
    # 例如，使用 OpenCV 的视频稳定功能
    # stabilized_frame = apply_stabilization(frame)

    out.write(frame)

cap.release()
out.release()