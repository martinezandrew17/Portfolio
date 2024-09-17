import customtkinter as ctk

class SimpleApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simple App")
        self.geometry("300x200")

        # Adding a Textbox
        self.output_text = ctk.CTkTextbox(self, width=300, height=100)
        self.output_text.pack(pady=20)

        # Adding a Button
        self.button = ctk.CTkButton(self, text="Add Text", command=self.add_text)
        self.button.pack(pady=10)

    def add_text(self):
        self.output_text.insert(ctk.END, "Sample text added.\n")

if __name__ == "__main__":
    app = SimpleApp()
    app.mainloop()
