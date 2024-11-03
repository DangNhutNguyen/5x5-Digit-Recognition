import numpy as np
from sklearn.linear_model import LogisticRegression
import tkinter as tk

# Define 5x5 representations of digits (0-9)
def generate_digit_patterns():
    # Basic digit patterns, represented as flattened 5x5 arrays
    digits = {
        0: [1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1],
        
        1: [0, 0, 1, 0, 0,
            0, 1, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 1, 1, 1, 0],
        
        2: [1, 1, 1, 1, 1,
            0, 0, 0, 0, 1,
            1, 1, 1, 1, 1,
            1, 0, 0, 0, 0,
            1, 1, 1, 1, 1],
        
        3: [1, 1, 1, 1, 1,
            0, 0, 0, 0, 1,
            0, 1, 1, 1, 1,
            0, 0, 0, 0, 1,
            1, 1, 1, 1, 1],
        
        4: [1, 0, 0, 1, 0,
            1, 0, 0, 1, 0,
            1, 1, 1, 1, 1,
            0, 0, 0, 1, 0,
            0, 0, 0, 1, 0],
        
        5: [1, 1, 1, 1, 1,
            1, 0, 0, 0, 0,
            1, 1, 1, 1, 1,
            0, 0, 0, 0, 1,
            1, 1, 1, 1, 1],
        
        6: [1, 1, 1, 1, 1,
            1, 0, 0, 0, 0,
            1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1],
        
        7: [1, 1, 1, 1, 1,
            0, 0, 0, 0, 1,
            0, 0, 0, 1, 0,
            0, 0, 1, 0, 0,
            0, 1, 0, 0, 0],
        
        8: [1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1],
        
        9: [1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1,
            0, 0, 0, 0, 1,
            1, 1, 1, 1, 1]
    }

    X = []
    y = []
    for digit, pattern in digits.items():
        for _ in range(10):  # Create 10 copies of each digit
            X.append(pattern)
            y.append(digit)
    
    return np.array(X), np.array(y)

# Train the model with the digit patterns
X_train, y_train = generate_digit_patterns()
logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train, y_train)

# Tkinter interface for drawing
class DrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw a Digit (5x5)")
        
        self.canvas = tk.Frame(root)
        self.canvas.pack()
        
        self.grid_size = 5
        self.pixels = np.zeros((self.grid_size, self.grid_size), dtype=int)
        
        self.buttons = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                button = tk.Button(self.canvas, width=2, height=1, command=lambda i=i, j=j: self.toggle_pixel(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
                
        self.guess_button = tk.Button(root, text="Guess the Number", command=self.guess_number)
        self.guess_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="Draw a number and press 'Guess the Number'")
        self.result_label.pack()
    
    def toggle_pixel(self, i, j):
        self.pixels[i][j] = 1 - self.pixels[i][j]
        color = "black" if self.pixels[i][j] == 1 else "white"
        self.buttons[i][j].config(bg=color)
    
    def guess_number(self):
        # Flatten 5x5 grid to match input shape for logistic regression model
        flat_pixels = self.pixels.flatten().reshape(1, -1)
        guess = logistic_model.predict(flat_pixels)
        self.result_label.config(text=f"Model's Guess: {guess[0]}")

# Run the app
root = tk.Tk()
app = DrawApp(root)
root.mainloop()
