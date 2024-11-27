import tkinter as tk
from tkinter import filedialog
import pandas as pd
class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Main Page Title
        title_label = tk.Label(
            self,
            text="Please Upload Your Workout",
            font=("Arial", 18),
            bg="red",
            bd=5,
            relief="solid"
        )
        title_label.pack(pady=20)

        # Styling fo for Buttons
        button_style = {
            "font": ("Arial", 18),
            "bg": "lightgreen",    
            "bd": 5,             
            "relief": "solid",   
            "width": 18,         
            "height": 2          
        }

        # Button 1 Manually
        button1 = tk.Button(
            self,
            text="Manually",
            **button_style,
            command=lambda: controller.show_frame("ManualFrame")  # Switch to ManualFrame
        )
        button1.pack(pady=10)

        # Button 2 Upload a File
        button2 = tk.Button(
            self,
            text="Upload a File",
            **button_style,
            command=lambda: self.upload_file(controller),
        )
        button2.pack(pady=10)

    #function to upload a file to the program 
    def upload_file(self, controller):
        # Open file to select file
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("Excel Files", "*.xlsx"), ("CSV Files", "*.csv")]
        )
        if file_path:
            # To Read the file using pandas
            try:
                if file_path.endswith(".xlsx"):
                    df = pd.read_excel(file_path, engine="openpyxl")  # Read Excel file
                elif file_path.endswith(".csv"):
                    df = pd.read_csv(file_path)  # Read CSV file
                else:
                    raise ValueError("Unsupported file format")

                # Convert the list in the file to a list of dictionaries
                data = df.to_dict(orient="records")

                # make sure the data as expected 
                required_columns = {"day", "steps", "calories", "time"}
                if not required_columns.issubset(df.columns):
                    raise ValueError("File is missing required columns: day, steps, calories, time")

                # Pass data to DisplayFrame
                display_frame = controller.frames["DisplayFrame"]
                display_frame.load_data(data)

                # go to Display frame 
                controller.show_frame("DisplayFrame")
                #if not do the error 
            except Exception as e:
                tk.messagebox.showerror(f"Failed to upload file: {str(e)}")


