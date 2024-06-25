import tkinter as tk
from tkinter import scrolledtext
import ttkbootstrap as ttk
import backend
import threading


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
        response = backend.get_response(message)
        self.chat_log.insert(tk.END, "ChatGPT: " + response + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    root["bg"] = "black"
    chat_bot = ChatBot(root)
    root.mainloop()