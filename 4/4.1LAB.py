import tkinter as tk
rainbow_colors = {
    "красный": "#FF0000",
    "оранжевый": "#FFA500",
    "желтый": "#FFFF00",
    "зеленый": "#008000",
    "голубой": "#42AAFF",
    "синий": "#0000FF",
    "фиолетовый": "#8B00FF"
}
class RainbowColors: 
    def __init__(self, master): 
        self.master = master
        self.master.title("Rainbow Colors") 
        self.color_label = tk.Label(text="выберите цвет")
        self.color_label.pack(pady=10) 
        self.color_entry = tk.Entry(state="readonly") 
        self.color_entry.pack(pady=10)
        self.create_color_buttons() 
    def create_color_buttons(self): 
        for color_name, color_code in rainbow_colors.items(): 
            button = tk.Button(text="\t\n\t", bg=color_code,command=lambda c=color_code, n=color_name: self.show_color(c,n))
            button.pack(side=tk.LEFT)
    def show_color(self, color_code,color_name): 
        self.color_label.config(text=color_name) 
        self.color_entry.config(state="normal") 
        self.color_entry.delete(0, tk.END) 
        self.color_entry.insert(0, color_code) 
        self.color_entry.config(state="readonly") 

def main():
    window = tk.Tk()
    app = RainbowColors(window)
    window.resizable(width=False, height=False)
    window.mainloop()
if __name__ == "__main__":
    main()
