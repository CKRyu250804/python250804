import os
import glob
import shutil

# 다운로드 폴더 경로
download_dir = r"C:\Users\student\Downloads"

# 이동할 폴더 경로
images_dir = os.path.join(download_dir, "images")
data_dir = os.path.join(download_dir, "data")
docs_dir = os.path.join(download_dir, "docs")
archive_dir = os.path.join(download_dir, "archive")

# 폴더가 없으면 생성
for folder in [images_dir, data_dir, docs_dir, archive_dir]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 파일 이동 함수
def move_files(patterns, target_dir):
    for pattern in patterns:
        for file in glob.glob(os.path.join(download_dir, pattern)):
            try:
                shutil.move(file, target_dir)
                print(f"{os.path.basename(file)} → {os.path.basename(target_dir)} 폴더로 이동")
            except Exception as e:
                print(f"{file} 이동 실패: {e}")

# 파일별로 이동
move_files(["*.jpg", "*.jpeg"], images_dir)
move_files(["*.csv", "*.xlsx"], data_dir)
move_files(["*.txt", "*.doc", "*.pdf"], docs_dir)
move_files(["*.zip", "*.rar", "*.tar"], archive_dir)