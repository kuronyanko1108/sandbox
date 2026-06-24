from PIL import Image
import pyocr
import pyocr.builders
from janome.tokenizer import Tokenizer
import json

# Tesseractの実行ファイルへのパスを指定
pyocr.tesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# OCRエンジンの選択
tools = pyocr.get_available_tools()
tool = tools[0]

# 画像のファイルを指定する
img_path = (
    "C:/Users/Sakan/dev/anki-snap-importer/capture/completed/20260623_question_004.png"
)
img = Image.open(img_path)

# 画像からテキストを抽出
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
txt = tool.image_to_string(img, lang="eng+jpn", builder=builder).replace(" ", "")


# 形態素解析
t = Tokenizer("user.csv", udic_type="simpledic", udic_enc="utf8")
words_set = set(token for token in t.tokenize(txt, wakati=True))

# JSONファイルの読み込み
with open("config.json", mode="r", encoding="utf-8") as f:
    tag_mapping = json.load(f)

# タグの設定
tag_set = set()
for word in words_set:
    if word in tag_mapping:
        tag_set.update(tag_mapping[word])

anki_tags = list(tag_set)

print(anki_tags)
