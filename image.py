from PIL import Image
import os

# 이미지 폴더 경로 설정
input_folder = 'ori'  # 원본 이미지들이 있는 폴더 경로
output_folder = 'frame'  # 결과물이 저장될 폴더 경로

# 프레임의 크기 설정 (6400x6400 픽셀)
frame_size = (6400, 6400)

# 출력 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 이미지 파일 일괄 처리
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # 지원하는 이미지 포맷
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # 이미지의 중앙에 배치될 새 캔버스(프레임) 생성
        frame = Image.new("RGB", frame_size, (255, 255, 255))  # 흰색 배경

        # 원본 이미지 크기 조정 (프레임 안에 맞도록)
        img.thumbnail((frame_size[0] - 100, frame_size[1] - 100))  # 여백을 두고 축소

        # 중앙 좌표 계산
        x = (frame_size[0] - img.width) // 2
        y = (frame_size[1] - img.height) // 2

        # 중앙에 이미지 붙여넣기
        frame.paste(img, (x, y))

        # 결과 이미지 저장
        output_path = os.path.join(output_folder, filename)
        frame.save(output_path)

        print(f"Processed {filename}")

print("모든 이미지 처리 완료.")