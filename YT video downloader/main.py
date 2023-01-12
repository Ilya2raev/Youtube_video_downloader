import tkinter as tk
from tkinter import ttk

import pafy
import os, sys


class Application(tk.Tk):
    """Название класса говорит за себя"""

    def __init__(self):
        """к̶о̶н̶с̶т̶р̶у̶к̶т̶о̶р̶  инициализатор класса"""
        super().__init__()
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        self.resizable(False, False)
        self.title('Youtube Video Downloader')

        self.run_ui()
    
    def run_ui(self):
        """Запуск интерфейса"""
        self.set_ui()

    def set_ui(self):
        """Построение интерфейса"""
        self.entry_label = ttk.Label(self, text='Insert valid YouTube link', padding=(5,15,0,0))
        self.entry_label.pack(fill=tk.X)

        self.entry_field = ttk.Entry(width=100)
        self.entry_field.pack(anchor=tk.N, padx=8, pady=8)

        self.download_button = ttk.Button(self, text='Download', command=lambda: self.download_video(self.entry_field.get()))
        self.download_button.pack(side=tk.LEFT)

        self.exit_button = ttk.Button(self, text='Exit', command=self.app_exit)
        self.exit_button.pack(anchor=tk.SE)
    
    def download_video(self, url):
        """Скачивание видео"""
        video = pafy.new(url)
        video.streams[0].download(quiet=True, filepath=os.getcwd())   
        
    def app_exit(self):
        """Выход из программы"""
        self.destroy()
        sys.exit()


if __name__ == '__main__':
    root = Application()
    root.iconphoto(False, tk.PhotoImage(file=os.getcwd() + '\icon.png'))
    root.mainloop()
    
