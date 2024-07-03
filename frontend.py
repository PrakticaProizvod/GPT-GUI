import tkinter as tk
import ttkbootstrap as ttk
import backend
import threading
from PIL import Image, ImageDraw, ImageTk


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

        threading.Thread(target=self.get_response, args=(message,)).start()

    def get_response(self, message):
        response = backend.get_response_text(message)
        self.chat_log.insert(tk.END, "ChatGPT: " + response + "\n")

        image = self.generate_image(response)
        self.display_image(image)

    def generate_image(self, text):
        img = Image.new('RGB', (400, 200), color='white')
        d = ImageDraw.Draw(img)
        d.text((10, 10), text, fill=(0, 0, 0))

        img_tk = ImageTk.PhotoImage(img)

        return img_tk

    def display_image(self, image):
        self.chat_log.image_create(tk.END, image=image)
        self.chat_log.insert(tk.END, "\n")


def main():
    root = tk.Tk()
    root["bg"] = "black"
    chat_bot = ChatBot(root)
    root.mainloop()


if __name__ == "__main__":
    main()