import tkinter as tk
from start import WelcomeFrame
from main import MainFrame
from manual_frame import ManualFrame
from display_frame import DisplayFrame

class App(tk.Tk): #main application class. inherits from tk.Tk
    def __init__(self):
        super().__init__() #call construction of the tk.Tk class
        #name and size of the app
        self.title("Fitness Tracker")
        self.geometry("370x640")

        # Container for frames, both make sure the frame expand H and V
        #true allow the dynmical resizeing
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Configure grid layout fo r the containers to ensure frames full size
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        #to store frames
        self.frames = {}

        # loop in the list of frames clases 
        for FrameClass in (WelcomeFrame, MainFrame, ManualFrame, DisplayFrame):
            frame = FrameClass(parent=container, controller=self)
            #parent to specifiy the frame belong to container, controller allows each frame to access the app instance
            self.frames[FrameClass.__name__] = frame #store the frame in self.frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show Welcome Frame
        self.show_frame("WelcomeFrame")

    def show_frame(self, frame_name):
        #to show and swithc the frames within the app 
        frame = self.frames[frame_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()  # Initialize the App
    app.mainloop()  # Run the Tkinter main event loop
