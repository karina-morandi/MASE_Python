import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def main():
        # Creating a sample DataFrame
        data = {'Category': ['A', 'B', 'C', 'D', 'E'],
                'Value': [10, 30, 20, 25, 15]}
        df = pd.DataFrame(data)
        # Create the main window
        root = tk.Tk()
        root.title("Classic Models")
        # Create a custom frame to hold the Matplotlib plot
        frame = ttk.Frame(root)
        frame.pack(expand=True, fill=tk.BOTH)
        # Create a Matplotlib figure and subplot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6), dpi=100)
        # Plotting a pie chart
        ax1.pie(df['Value'], labels=df['Category'], autopct='%1.1f%%', startangle=90,)
        ax1.set_title('Pie Chart')
        # Plotting a bar chart with 'tab10' colors
        ax2.bar(df['Category'], df['Value'])
        ax2.set_xlabel('Category')
        ax2.set_ylabel('Value')
        ax2.set_title('Bar Chart')
        # Create a Matplotlib canvas within the frame
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        # Add a toolbar (optional)
        from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        toolbar = NavigationToolbar2Tk(canvas, frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        toolbar.update()
        # Start the Tkinter main loop
        root.mainloop()

if __name__ == '__main__':
        main()