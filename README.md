# 🃏 One Piece Live Queue Manager PRO

ระบบจัดการคิวและออเดอร์สำหรับ **Live สดขายการ์ด One Piece** พัฒนาด้วย Python โดยใช้หลักการ **Object-Oriented Programming (OOP)**

---

## 📌 เกี่ยวกับโปรเจกต์

โปรเจกต์นี้เป็นส่วนหนึ่งของวิชา **Object-Oriented Programming**  
สร้างแอปพลิเคชัน GUI สำหรับช่วยผู้ขายจัดการคิว, ออเดอร์, และสต็อกสินค้าระหว่างการไลฟ์สดขายการ์ด One Piece Trading Card Game

---

## ✨ ฟีเจอร์หลัก

- 📦 **จัดการสต็อกสินค้า** — แสดงรูปการ์ด, ราคา, และจำนวนคงเหลือแบบ Real-time
- 🛒 **รับออเดอร์** — เพิ่มคิวลูกค้าพร้อมเลือกสินค้าและจำนวน
- 🔄 **ระบบสถานะออเดอร์** — `Pending` → `Paid` → `Opened`
- ✅ **ยืนยันการชำระเงิน** — กดยืนยันโอนเงินเพื่ออัปเดตสถานะ
- 💰 **แสดงยอดขายรวม** — คำนวณและแสดงยอดขายทั้งหมดแบบ Real-time
- 🎨 **GUI สวยงาม** — ใช้ ttkbootstrap theme "superhero"

---

## 🗂 โครงสร้างโปรเจกต์

```
OOP-Project/
├── my_rpg_game/
│   ├── main.py         # จุดเริ่มต้นโปรแกรม
│   ├── app_gui.py      # ส่วน GUI (tkinter + ttkbootstrap)
│   ├── systems.py      # Business Logic (Inventory, LiveManager)
│   ├── models.py       # Data Models (CardSet, Order)
│   └── config.py       # ค่าคงที่และ Path รูปภาพ
├── assets/
│   ├── OP-05.jpg
│   ├── OP-06.jpg
│   └── OP-13.jpg
└── README.md
```

---

## 🧩 แนวคิด OOP ที่ใช้

| หลักการ | ตัวอย่างในโปรเจกต์ |
|---|---|
| **Encapsulation** | `__stock` ใน `CardSet` และ `__orders` ใน `LiveManager` เป็น Private Attribute |
| **Abstraction** | Method `get_total()` ซ่อนการคำนวณราคา, `reduce_stock()` ซ่อน Logic การลดสต็อก |
| **Composition** | `Order` มี `CardSet` เป็น Attribute (Order ประกอบด้วย CardSet) |
| **Property** | ใช้ `@property` สำหรับ `stock` เพื่อควบคุมการเข้าถึง |
| **Class & Object** | แยก Class ชัดเจน: `CardSet`, `Order`, `Inventory`, `LiveManager`, `ProductCard` |

---

## 🚀 การติดตั้งและรันโปรแกรม

### 1. ติดตั้ง Dependencies

```bash
pip install ttkbootstrap Pillow
```

### 2. เตรียมรูปภาพ

วางไฟล์รูปการ์ดไว้ในโฟลเดอร์ `assets/`

```
assets/
├── OP-05.jpg
├── OP-06.jpg
└── OP-13.jpg
```

### 3. รันโปรแกรม

```bash
python main.py
```

---

## 🖥️ วิธีใช้งาน

1. **ดูสต็อก** — ฝั่งซ้ายจะแสดงการ์ดที่มีในสต็อกพร้อมรูป, ราคา, และจำนวนคงเหลือ
2. **รับออเดอร์** — กรอกชื่อลูกค้า, เลือกสินค้า, ใส่จำนวน แล้วกด **เพิ่มลงคิว**
3. **ยืนยันโอนเงิน** — เลือกออเดอร์ในตาราง แล้วกด **✅ ยืนยันโอนเงิน** (สถานะเปลี่ยนเป็น `Paid` ไฮไลต์สีเขียว)
4. **เปิดการ์ด** — กด **📦 เปิดการ์ดแล้ว** เมื่อส่งของให้ลูกค้าเสร็จ (สถานะเปลี่ยนเป็น `Opened` และหายจากคิว)
5. **ยอดขาย** — แสดงที่มุมขวาบนแบบ Real-time

---

## 📦 สินค้าในระบบ (Default)

| Set ID | ชื่อ | ราคา/ซอง | สต็อกเริ่มต้น |
|---|---|---|---|
| OP05 | OP-05 | 320.- | 100 ซอง |
| OP06 | OP-06 | 380.- | 80 ซอง |
| OP13 | OP-13 | 480.- | 50 ซอง |

---

## 🛠 Dependencies

| Package | การใช้งาน |
|---|---|
| `ttkbootstrap` | GUI Framework + Theme |
| `Pillow` | แสดงรูปภาพสินค้า |
| `tkinter` | GUI พื้นฐาน (มาพร้อม Python) |
| `datetime` | บันทึก Timestamp ออเดอร์ |

---

## 👤 ผู้พัฒนา

**noomsky12345**  
โปรเจกต์วิชา Object-Oriented Programming
