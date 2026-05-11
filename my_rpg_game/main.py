import ttkbootstrap as ttk
from app_gui import LiveAppPro
import config

if __name__ == "__main__":
    root = ttk.Window(themename=config.THEME)
    app = LiveAppPro(root)
    root.mainloop()