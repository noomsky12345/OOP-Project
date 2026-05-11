import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk  # ต้องมี Pillow
import config
from systems import LiveManager
from models import CardSet

class ProductCard(ttk.Frame):
    """Component สำหรับแสดงรูปสินค้าในสต็อก (เพิ่มการแสดงราคา)"""
    def __init__(self, parent, card_set_obj):
        super().__init__(parent, bootstyle=SECONDARY, padding=10)
        self.card_set = card_set_obj
        
        # จัดการรูปภาพ
        try:
            img = Image.open(self.card_set.img_path)
            img = img.resize((80, 110), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            ttk.Label(self, image=self.photo, bootstyle=SECONDARY).pack()
        except:
            ttk.Label(self, text="No Image", width=10).pack()

        self.lbl_name = ttk.Label(self, text=self.card_set.name, font=("Arial", 10, "bold"))
        self.lbl_name.pack(pady=(5, 0))
        
        # --- ส่วนที่เพิ่มใหม่: แสดงราคา ---
        self.lbl_price = ttk.Label(self, text=f"{self.card_set.price}.- / ซอง", bootstyle=WARNING, font=("Arial", 9, "bold"))
        self.lbl_price.pack()

        self.lbl_stock = ttk.Label(self, text=f"คงเหลือ: {self.card_set.stock}", bootstyle=INFO, font=("Arial", 8))
        self.lbl_stock.pack(pady=(2, 0))

class LiveAppPro:
    def __init__(self, root):
        self.root = root
        self.root.title("One Piece Live Queue Manager PRO")
        self.root.geometry("1200x800")
        
        self.manager = LiveManager()
        self.__init_data()

        # Main Layout
        container = ttk.Frame(self.root, padding=20)
        container.pack(fill=BOTH, expand=YES)

        # --- Left: Inventory & Input ---
        left_side = ttk.Frame(container, width=400)
        left_side.pack(side=LEFT, fill=BOTH, padx=(0, 20))

        ttk.Label(left_side, text="📦 คลังสินค้าปัจจุบัน", font=("Arial", 16, "bold")).pack(anchor=W, pady=10)
        
        # พื้นที่โศว์รูปสินค้า
        self.stock_frame = ttk.Frame(left_side)
        self.stock_frame.pack(fill=X, pady=10)
        
        ttk.Separator(left_side).pack(fill=X, pady=20)
        
        # Form
        ttk.Label(left_side, text="👤 รับออเดอร์ใหม่", font=("Arial", 14, "bold")).pack(anchor=W)
        ttk.Label(left_side, text="ชื่อลูกค้า:").pack(anchor=W, pady=5)
        self.ent_name = ttk.Entry(left_side)
        self.ent_name.pack(fill=X)

        ttk.Label(left_side, text="เลือกสินค้า:").pack(anchor=W, pady=5)
        self.cb_sets = ttk.Combobox(left_side, state="readonly")
        self.cb_sets.pack(fill=X)

        ttk.Label(left_side, text="จำนวน:").pack(anchor=W, pady=5)
        self.ent_qty = ttk.Spinbox(left_side, from_=1, to=100)
        self.ent_qty.set(1)
        self.ent_qty.pack(fill=X)

        ttk.Button(left_side, text="เพิ่มลงคิว", bootstyle=SUCCESS, command=self.add_order).pack(fill=X, pady=20)

        # --- Right: Queue & Sales ---
        right_side = ttk.Frame(container)
        right_side.pack(side=LEFT, fill=BOTH, expand=YES)

        header_f = ttk.Frame(right_side)
        header_f.pack(fill=X)
        ttk.Label(header_f, text="🔥 คิวในไลฟ์", font=("Arial", 16, "bold")).pack(side=LEFT)
        self.lbl_sales = ttk.Label(header_f, text="ยอดขาย: 0.00.-", font=("Arial", 16, "bold"), bootstyle=SUCCESS)
        self.lbl_sales.pack(side=RIGHT)

        # Treeview
        self.tree = ttk.Treeview(right_side, columns=("Name", "Item", "Qty", "Total", "Status"), show=HEADINGS)
        for col in ("Name", "Item", "Qty", "Total", "Status"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill=BOTH, expand=YES, pady=10)

        # Control Buttons
        btn_f = ttk.Frame(right_side)
        btn_f.pack(fill=X)
        ttk.Button(btn_f, text="✅ ยืนยันโอนเงิน", bootstyle=INFO, command=self.confirm_pay).pack(side=RIGHT, padx=5)
        ttk.Button(btn_f, text="📦 เปิดการ์ดแล้ว", bootstyle=DANGER, command=self.finish_order).pack(side=RIGHT, padx=5)

        self.refresh_ui()

    def __init_data(self):
        """อัปเดตข้อมูลราคาตามที่คุณแจ้งมา"""
        # ID, ชื่อ, สต็อก, ราคา, รูปภาพ
        self.manager.inventory.add_item(CardSet("OP05", "OP-05", 100, 320, config.IMG_OP05))
        self.manager.inventory.add_item(CardSet("OP06", "OP-06", 80, 380, config.IMG_OP06))
        self.manager.inventory.add_item(CardSet("OP13", "OP-13", 50, 480, config.IMG_BOX)) # เปลี่ยนเป็น OP-13 ราคา 480

    def add_order(self):
        name = self.ent_name.get()
        sel = self.cb_sets.get()
        if not name or not sel: return
        set_id = sel.split("(")[1].strip(")")
        
        order, msg = self.manager.create_order(name, set_id, int(self.ent_qty.get()))
        if order:
            self.refresh_ui()
            self.ent_name.delete(0, END)
        else:
            messagebox.showwarning("Error", msg)

    def confirm_pay(self):
        sel = self.tree.selection()
        if not sel: return
        name = self.tree.item(sel[0])['values'][0]
        if self.manager.confirm_payment(name):
            self.refresh_ui()

    def finish_order(self):
        if self.manager.finish_order():
            self.refresh_ui()

    def refresh_ui(self):
        # 1. ล้างและวาด Stock Cards ใหม่
        for widget in self.stock_frame.winfo_children():
            widget.destroy()
        
        item_names = []
        for i, item in enumerate(self.manager.inventory.get_all()):
            card = ProductCard(self.stock_frame, item)
            card.grid(row=0, column=i, padx=5)
            item_names.append(f"{item.name} ({item.set_id})")
        self.cb_sets['values'] = item_names

        # 2. Update Queue
        self.tree.delete(*self.tree.get_children())
        for o in self.manager.get_queue():
            tag = 'paid' if o.status == "Paid" else 'pending'
            self.tree.insert("", END, values=(o.customer_name, o.card_set.name, o.quantity, o.get_total(), o.status), tags=(tag,))
        self.tree.tag_configure('paid', background='#2d3e50', foreground='#00ff00') # สีเขียวเด่นๆ
        
        self.lbl_sales.config(text=f"ยอดขายรวม: {self.manager.get_total_sales():,.2f}.-")