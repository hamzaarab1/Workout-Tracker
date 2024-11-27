import tkinter as tk
from tkinter import ttk

class ManualFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.row_counter = 0 #this to start the day in here
        self.used_days = []  # Track used days
        self.data = []  # Store the input in here

        # Title Label for the Page
        title_label = tk.Label(
            self,
            text="Manual Input Page",
            font=("Arial", 12),
            bg="lightblue",
            bd=2,
            relief="solid"
        )
        title_label.pack(pady=5)

        # Frame for Input Table
        self.table_frame = tk.Frame(self, bg="black", bd=1, relief="solid")
        self.table_frame.pack(pady=5, fill="x", padx=10)

        # Header Row
        headers = ["Day", "Steps", "Calories", "Time (min)"]
        for col, header in enumerate(headers):
            header_label = tk.Label(
                self.table_frame,
                text=header,
                font=("Arial", 10),
                bg="lightblue",
                bd=1,
                relief="solid",
                width=10
            )
            header_label.grid(row=0, column=col, sticky="nsew", padx=1, pady=1)

        # Add Button
        self.add_button = tk.Button(
            self,
            text="+",
            font=("Arial", 14),
            bg="lightblue",
            bd=2,
            relief="solid",
            command=self.add_row
        )
        self.add_button.pack(pady=5)

        # Done Button
        self.done_button = tk.Button(
            self,
            text="Done",
            font=("Arial", 14),
            bg="lightgreen",
            bd=2,
            relief="solid",
            command=self.store_data_and_navigate  # Collect data and go to display 
        )
        self.done_button.pack(pady=5)

    def add_row(self):
        # Limit the input to 7 days 
        if self.row_counter >= 7:
            return

        # Making a Selection
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        day_dropdown = ttk.Combobox(
            self.table_frame,
            values=[day for day in days_of_week if day not in self.used_days],
            state="readonly",
            width=8
        )
        day_dropdown.grid(row=self.row_counter + 1, column=0, padx=1, pady=1)

        # Input fields for Steps, Calories, Time
        steps_entry = tk.Entry(self.table_frame, width=10, justify="center")
        steps_entry.grid(row=self.row_counter + 1, column=1, padx=1, pady=1)

        calories_entry = tk.Entry(self.table_frame, width=10, justify="center")
        calories_entry.grid(row=self.row_counter + 1, column=2, padx=1, pady=1)

        time_entry = tk.Entry(self.table_frame, width=10, justify="center")
        time_entry.grid(row=self.row_counter + 1, column=3, padx=1, pady=1)

        # Track the selected day
        def track_day(event):
            if day_dropdown.get() not in self.used_days:
                self.used_days.append(day_dropdown.get()) #to make sure days aren't repeated 
                day_dropdown["values"] = [day for day in days_of_week if day not in self.used_days]

        day_dropdown.bind("<<ComboboxSelected>>", track_day)

        # Add input references to self.data for later access
        self.data.append({
            "day": day_dropdown,
            "steps": steps_entry,
            "calories": calories_entry,
            "time": time_entry
        })

        self.row_counter += 1

        # Move the add button below the last row if a row is added 
        self.add_button.pack_forget()
        self.add_button.pack(pady=5)
        self.done_button.pack_forget()
        self.done_button.pack(pady=5)

    def store_data_and_navigate(self):
        # Collect and store all data
        stored_data = []
        for row in self.data:
            day = row["day"].get()
            steps = row["steps"].get()
            calories = row["calories"].get()
            time = row["time"].get()
            if day and steps and calories and time:  # Only save if all fields are filled if not ignore it
                #to make sure no empty columns don't get stored 
                stored_data.append({
                    "day": day,
                    "steps": int(steps),
                    "calories": int(calories),
                    "time": int(time)
                })

        # Pass data to the DisplayFrame
        display_frame = self.controller.frames["DisplayFrame"]
        display_frame.load_data(stored_data)

        # Navigate to the DisplayFrame
        self.controller.show_frame("DisplayFrame")