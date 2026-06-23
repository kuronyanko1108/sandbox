from PIL import Image
import pyocr
import pyocr.builders

# Tesseractの実行ファイルへのパスを指定
pyocr.tesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# OCRエンジンの選択
tools = pyocr.get_available_tools()
tool = tools[0]

# 画像のファイルを指定する
img_path = (
    "C:/Users/Sakan/dev/anki-snap-importer/capture/completed/20260623_question_008.png"
)
img = Image.open(img_path)

# 画像からテキストを抽出
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
txt = tool.image_to_string(img, lang="eng+jpn", builder=builder).replace(" ", "")

builder = pyocr.builders.WordBoxBuilder(tesseract_layout=6)
boxs = tool.image_to_string(img, lang="eng+jpn", builder=builder)


print(txt)
print("Yes" if ">データベース" in txt else "No")
