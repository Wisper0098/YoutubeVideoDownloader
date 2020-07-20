import pafy
from tkinter import *
from tkinter import filedialog


class Utube_downloader():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x150')
        self.root.resizable(width=False, height=False)
        self.root.title('YouTube Downloader')
        self.root.wm_attributes('-alpha', 0.9)
        self.root.iconbitmap(r'utube_icon.ico')
        self.root['bg'] = '#d1d3de'
        self.url = Entry(self.root, font='Consolas 15', relief='solid', justify='center')
        self.url_text = Label(self.root, text="URL:", font='12', bg='#d1d3de')
        self.error_message = Label(self.root, text="Wrong url!", bg='#d1d3de')
        self.download_button = Button(self.root, text='Download HD', command=self.download_hd)
        self.downloadMp3_button = Button(self.root, text='Download AUDIO', command=self.download_mp3)
        self.url.pack()
        self.download_button.place(x=155, y=28)
        self.downloadMp3_button.place(x=250, y=28)
        self.url_text.place(x=87, y=0)
        self.root.mainloop()

    def download_hd(self):
        URL = self.url.get()
        if URL.startswith('https://www.youtube'):
            self.root.path = filedialog.askdirectory(initialdir="C:/", title="Choose filepath")
            video = pafy.new(URL) 
            best = video.getbest(preftype="mp4") # find file with best resolution in mp4 format.
            best.download(filepath=self.root.path) # download to file path 

        else:
            self.error_message.place(x=220, y=100)

    def download_mp3(self):
        URL = self.url.get()
        if URL.startswith('https://www.youtube'):
            self.root.path = filedialog.askdirectory(initialdir="C:/", title="Choose filepath")
            video = pafy.new(URL)
            bestaudio = video.getbestaudio(preftype="m4a") # m4a is audio type
            bestaudio.download(filepath=self.root.path)

        else:
            self.error_message.place(x=220, y=100)


