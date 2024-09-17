import customtkinter as ctk

class SimpleApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simple App")
        self.geometry("300x200")

        self.label = ctk.CTkLabel(self, text="Hello, world!")
        self.label.pack(pady=20)

if __name__ == "__main__":
    app = SimpleApp()
    app.mainloop()
