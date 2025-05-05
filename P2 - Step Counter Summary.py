# a pink step counter
#import needed tools
import tkinter as tk
from tkinter import messagebox
#global variable input
Weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#start scaling

class StepTrackerBase:
    def __init__(self, root):
        self.root = root
        self.root.title("Stepcount Tracker")
        self.root.configure(bg="#ffc0cb")
        self.root.geometry("500x500")

        #needed variables
        self.week_index = 1
        self.total_steps = 0
        self.weeks = 0

        self.create_widgets()

    def create_widgets(self):
        self.clear_window()

        tk.Label(self.root, text="Enter number of weeks to track:", bg="#ffc0cb", font=("Arial", 12)).pack(pady=10)
        self.weeks_entry = tk.Entry(self.root)
        self.weeks_entry.pack(pady=5)

        tk.Button(self.root, text="Start Tracking", command=self.initiate_tracking, bg="#ff69b4", fg="white").pack(pady=10)

    def initiate_tracking(self):
        try:
            self.weeks = int(self.weeks_entry.get())
            if self.weeks <= 0:
                raise ValueError
            self.total_steps = 0
            self.week_index = 1
            self.ask_for_week_steps()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a positive number of weeks.")

    def ask_weekly_steps(self):
        self.clear_window()

        tk.Label(self.root, text=f"Week {self.week_index}", bg="#ffc0cb", font=("Arial", 14, "bold")).pack(pady=10)

        self.day_entries = {}
        for day in Weekdays:
            frame = tk.Frame(self.root, bg="#ffc0cb")
            frame.pack(pady=2)
            tk.Label(frame, text=f"{day}:", width=10, anchor="w", bg="#ffc0cb", font=("Arial", 10)).pack(side="left")
            entry = tk.Entry(frame, width=10)
            entry.pack(side="left")
            self.day_entries[day] = entry

        tk.Button(self.root, text="Submit Week", command=self.submit_week, bg="#ff69b4", fg="white").pack(pady=20)

    def submit_week(self):
        try:
            for day in Weekdays:
                steps = int(self.day_entries[day].get())
                if steps < 0:
                    raise ValueError
                self.total_steps += steps

            if self.week_index < self.weeks:
                self.week_index += 1
                self.ask_for_week_steps()
            else:
                self.show_summary()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter non-negative integers for all days.")

    def stepsummary(self):
        self.clear_window()
        total_days = self.weeks * 7
        avg_steps = self.total_steps / total_days

        summary = (
            f"You walked for {total_days} days.\n"
            f"Total steps taken: {self.total_steps:,}\n"
            f"Average steps per day: {avg_steps:.2f}\n"
            "Awesome work!"
        )

        tk.Label(self.root, text=summary, bg="#ffc0cb", font=("Arial", 12), justify="left").pack(pady=30)

        tk.Button(self.root, text="Restart", command=self.create_intro_widgets, bg="#ff69b4", fg="white").pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, bg="#ff69b4", fg="white").pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = StepTrackerBase(root)
    root.mainloop()
