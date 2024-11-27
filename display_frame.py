import tkinter as tk
class DisplayFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.data = []  # array for input data

        # Average Button
        self.average_button = tk.Button(
            self,
            text="Calculate Average",
            font=("Arial", 12),
            bg="lightyellow",
            bd=2,
            relief="solid",
            command=self.calculate_averages
        )
        self.average_button.pack(pady=5)

        # Results Frame for Averages
        self.results_frame = tk.Frame(self)
        self.results_frame.pack(pady=10)

        # Total Calories Button
        self.total_calories_button = tk.Button(
            self,
            text="Total Calories Burned",
            font=("Arial", 12),
            bg="lightgreen",
            bd=2,
            relief="solid",
            command=self.calculate_total_calories
        )
        self.total_calories_button.pack(pady=5)

        # Total Calories Frame
        self.total_calories_frame = tk.Frame(self)
        self.total_calories_frame.pack(pady=10)

        # Day with the Maximum Steps Button
        self.Maximum_day = tk.Button(
            self,
            text="Day with the Maximum Steps",
            font=("Arial", 12),
            bg="orange",
            bd=2,
            relief="solid",
            command=self.find_day
        )
        self.Maximum_day.pack(pady=5)

        # Best Day Frame
        self.best_day = tk.Frame(self)
        self.best_day.pack(pady=10)

        # Back to Main Button
        self.back_to_main_button = tk.Button(
            self,
            text="Add a Different Week",
            font=("Arial", 12),
            bg="red",
            bd=2,
            relief="solid",
            command=lambda: controller.show_frame("MainFrame")  # Switch to MainFrame
        )
        self.back_to_main_button.pack(pady=10)

    def load_data(self, data):
        # Load the data from the one passed in Manual frame
        self.data = data  # Save the data for calculations

    def calculate_averages(self):
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # Calculate averages
        total_days = len(self.data)
        total_steps = sum(entry["steps"] for entry in self.data)
        total_calories = sum(entry["calories"] for entry in self.data)
        total_time = sum(entry["time"] for entry in self.data)

        avg_steps = total_steps / total_days if total_days > 0 else 0
        avg_calories = total_calories / total_days if total_days > 0 else 0
        avg_time = total_time / total_days if total_days > 0 else 0

        # Display the averages in three smaller circles
        self.create_result_circle(self.results_frame, "Steps", round(avg_steps, 2), 8, 3)
        self.create_result_circle(self.results_frame, "Calories", round(avg_calories, 2), 8, 3)
        self.create_result_circle(self.results_frame, "Time (min)", round(avg_time, 2), 8, 3)

    def calculate_total_calories(self):
        # Clear previous total calories result
        for widget in self.total_calories_frame.winfo_children():
            widget.destroy()

        # Calculate total calories
        total_calories = sum(entry["calories"] for entry in self.data)

        # Display the total calories in a larger circle
        self.create_result_circle(self.total_calories_frame, "Total Calories", total_calories, 12, 6)

    def find_day(self):
        # Clear previous results in the best_day frame
        for widget in self.best_day.winfo_children():
            widget.destroy()

        if not self.data:
            # Handle the case where no data is available
            self.create_result_circle(self.best_day, "No Data", "N/A", 12, 6)
            return

        # Find the entry with the maximum steps
        max_entry = max(self.data, key=lambda entry: entry["steps"])
        day_with_max_steps = max_entry["day"]
        max_steps = max_entry["steps"]

        # Display the result in the best_day frame
        self.create_result_circle(
            self.best_day,
            f"{day_with_max_steps}",
            f"{max_steps} Steps",
            12,
            6
        )

    def create_result_circle(self, parent, label, value, width, height):
        #create a box to display the result 
        frame = tk.Frame(parent, width=140 if width == 12 else 80, height=140 if height == 6 else 80, bg="white", relief="solid", bd=2)
        frame.pack_propagate(False)  # Prevent auto-sizing
        frame.pack(side="left", padx=5)

        # Circle Label
        circle_label = tk.Label(
            frame,
            text=f"{label}\n{value}",
            font=("Arial", 10),
            bg="lightblue",
            relief="solid",
            bd=2,
            width=width,
            height=height,
            justify="center"
        )
        circle_label.pack(expand=True)
