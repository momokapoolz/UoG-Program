from tkinter import *
import tkinter.scrolledtext as tkst

import video_library as lib


def set_text(text_area, content): #create a text area to display the content
    text_area.delete("1.0", END)
    text_area.insert(1.0, content)


class CheckVideos():
    def __init__(self, window):
        window.geometry("1000x600")
        window.title("Check Videos")
        window.configure(background= "#333333")

        list_videos_btn = Button(window, text="List All Videos", command=self.list_videos_clicked,  background="#458B74")
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = Label(window, text="Enter Video Number",  background="#458B74")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = Button(window, text="Check Video", command=self.check_video_clicked,  background="#458B74")
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = Label(window, text="", font=("Helvetica", 10),  background="#458B74")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()



    def check_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")


    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")



