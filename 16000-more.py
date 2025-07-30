import os
import subprocess
from pathlib import Path

def convert_audio_sampling_rate(video_path, output_dir, sample_rate=16000, channels=1):
    """
    使用ffmpeg将视频文件的音频采样率转换为指定值，并设置为单声道。
    
    :param video_path: 输入视频文件路径
    :param output_dir: 输出文件保存的目录
    :param sample_rate: 目标音频采样率，默认为16000 Hz
    :param channels: 目标音频通道数，默认为1（单声道）
    """
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取文件名（不包括扩展名）和文件扩展名
    file_name = Path(video_path).stem
    file_ext = Path(video_path).suffix
    output_file = os.path.join(output_dir, f"{file_name}{file_ext}")
    
    # 构建ffmpeg命令
    command = [
        'ffmpeg', '-i', video_path,
        '-ar', str(sample_rate),  # 设置音频采样率为16000Hz
        '-ac', str(channels),     # 设置音频通道数为1（单声道）
        '-c:v', 'copy',           # 不重新编码视频流
        '-y',                     # 如果输出文件已存在，则覆盖
        output_file
    ]
    
    try:
        # 执行命令
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"成功转换: {video_path} -> {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"转换失败: {video_path}, 错误信息: {e.stderr.decode()}")

def process_directory(input_root_dir, output_root_dir):
    """
    遍历输入根目录及其子目录，处理其中的视频文件，并将结果保存到对应的输出目录。
    
    :param input_root_dir: 输入根目录路径
    :param output_root_dir: 输出根目录路径
    """
    for subdir in os.listdir(input_root_dir):
        input_subdir_path = os.path.join(input_root_dir, subdir)
        if os.path.isdir(input_subdir_path):
            # 创建对应的输出子文件夹
            output_subdir_path = os.path.join(output_root_dir, subdir)
            os.makedirs(output_subdir_path, exist_ok=True)

            for file_name in os.listdir(input_subdir_path):
                file_path = os.path.join(input_subdir_path, file_name)
                if os.path.isfile(file_path) and file_name.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
                    convert_audio_sampling_rate(file_path, output_subdir_path)

if __name__ == "__main__":
    input_root_directory = "300-000"  # 替换为你的输入根目录路径
    output_root_directory = "data"  # 替换为你的输出根目录路径
    process_directory(input_root_directory, output_root_directory)