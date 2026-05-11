import os

# หา Path ของโฟลเดอร์ assets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# ค้นหาไฟล์รูป (ถ้าไม่มีรูปเครื่องจะรันเป็นสีพื้นแทน)
IMG_OP05 = os.path.join(ASSETS_DIR, "OP-05.jpg")
IMG_OP06 = os.path.join(ASSETS_DIR, "OP-06.jpg")
IMG_BOX = os.path.join(ASSETS_DIR, "OP-13.jpg")

THEME = "superhero"