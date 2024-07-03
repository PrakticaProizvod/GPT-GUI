import tkinter as tk
import ttkbootstrap as ttk
import backend
import threading
from PIL import Image, ImageTk
import os


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Bot")
        self.root.geometry("1000x750")

        self.style = ttk.Style()
        self.style.theme_use("minty")

        self.chat_log = ttk.ScrolledText(self.root, width=120, height=30, font=("Arial", 12))
        self.chat_log.pack(padx=10, pady=10, fill="both", expand=True)

        self.entry = ttk.Entry(self.root, width=90, font=("Arial", 12))
        self.entry.pack(padx=10, pady=10)

        self.send_button = ttk.Button(self.root, text="Отправить", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

        self.entry.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        message = self.entry.get()
        self.chat_log.insert(tk.END, "User: " + message + "\n")

        self.entry.delete(0, tk.END)

        if message.startswith("/photo"):
            threading.Thread(target=self.get_response_image, args=(message[6:],)).start()
        else:
            threading.Thread(target=self.get_response, args=(message,)).start()

    def get_response(self, message):
        response_text = backend.get_response_text(message)
        self.chat_log.insert(tk.END, "ChatGPT: " + response_text + "\n")

    def get_response_image(self, message):
        backend.get_response_photo(message)
        image = Image.open("image.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.chat_log, image=photo)
        label.image = photo
        self.chat_log.window_create(tk.END, window=label)
        self.chat_log.insert(tk.END, "\n")

        os.remove("image.png")


def main():
    root = tk.Tk()
    root["bg"] = "black"
    chat_bot = ChatBot(root)
    root.mainloop()


if __name__ == "__main__":
    main()