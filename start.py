import tkinter as tk
from PIL import Image, ImageTk

class WelcomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # Welcome message 1
        welcome_label = tk.Label(
            self,
            text="Welcome to your Weekly",  
            font=("Arial", 22),
            bg="lightblue", 
            bd=5,
            relief="solid"
        )
        welcome_label.pack(pady=20)

        # Welcome message 2
        welcome_label2 = tk.Label(
            self,
            text="Fitness Tracker",  
            font=("Arial", 22),
            bg="lightblue", 
            bd=5,
            relief="solid"
        )
        welcome_label2.pack(pady=20)

        # upload the image path and display it
        image_path = "Images/Fitness_Image.webp"
        image = Image.open(image_path).resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo)
        image_label.image = photo
        image_label.pack(pady=20)
        # Switch to the main page after 3 seconds
        self.after(5000, lambda: controller.show_frame("MainFrame"))
