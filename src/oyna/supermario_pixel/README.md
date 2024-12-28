### Game Documentation: **Super Mario Art Display**

---

#### **Overview**
This is a simple Python program that displays animated Super Mario art using ASCII and emoji characters. The art changes every 0.5 seconds to create an animated effect. This is not a traditional game with user interaction but rather a fun way to showcase Super Mario-themed images in the terminal or console.

---

#### **How to Play/Use**

1. **Start the program**: The animation will start automatically once the program is run.
2. **Animation**: Two different Super Mario-themed art images will cycle in the terminal, switching every 0.5 seconds.
3. **Exit the Program**: The program will keep running until you manually stop it. To exit, you can press `Ctrl+C` in the terminal.

---

#### **Algorithm (Code Explanation)**

1. **Images Array**: The program stores a list of pre-defined Super Mario images represented using emojis and ASCII characters. Each image is a string formatted to fit into a terminal or console window.

2. **`cycle()` Function**: The program uses the `cycle()` function from Python's `itertools` module. This function will repeatedly cycle through the images infinitely, ensuring that the animation keeps playing.

3. **Clear Screen**: Every time the image is printed, the screen is cleared first with the ANSI escape code `\033[H\033[J`. This is done to ensure that each frame of the animation overwrites the previous frame, providing a smooth animation.

4. **Sleep Function**: The `sleep(0.5)` command causes the program to pause for 0.5 seconds between displaying each image, creating the animation effect.

---

#### **How to Install and Run the Code**

**Prerequisites**:
- Python 3.x installed on your system.

1. **Download the Code**:
   - Copy the code provided into a Python file (e.g., `grid_base.py`).

2. **Install Dependencies**:
   - There are no external libraries required to run the script. It only uses built-in Python modules.

3. **Run the Program**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the `grid_base.py` file is saved.
   - Run the program by typing:
     ```bash
     python grid_base.py
     ```

4. **Stop the Program**:
   - To stop the animation, simply press `Ctrl+C` in your terminal.

---

#### **Important Notes**
- The animation may vary depending on the size and resolution of your terminal window.
- If the terminal window is too small, the images may not display correctly.
- This is a fun animation program and not a traditional interactive game.

## Example Output:
```

          🟥🟥🟥🟥🟥    🟨🟨🟨
        🟥🟥🟥🟥🟥🟥🟥🟥🟥🟨🟨
        🟫🟫🟫🟨🟨⬛️🟨  🟥🟥🟥
      🟫🟨🟫🟨🟨🟨⬛️🟨🟨🟨🟥🟥
      🟫🟨🟫🟫🟨🟨🟨⬛️🟨🟨🟨🟥
        🟫🟨🟨🟨🟨⬛️⬛️⬛️⬛️🟥🟥    ♥️  SUPER MARIO ♥️
          🟨🟨🟨🟨🟨🟨🟥🟥🟥
        🟥🟥🟦🟥🟥🟦🟥🟥🟥
      🟥🟥🟥🟦🟥🟥🟦🟥🟥🟥
    🟥🟥🟥🟥🟦🟥🟥🟦🟥🟥
    🟨🟨🟥🟥🟦🟦🟦🟦🟥🟥
    🟨🟨🟨🟦🟦🟦🟦🟦🟦🟦
    🟨🟨🟦🟦🟦🟦🟦🟦🟦🟦
        🟦🟦🟦    🟦🟦🟦
      🟫🟫🟫        🟫🟫🟫
    🟫🟫🟫🟫        🟫🟫🟫🟫
```

Enjoy watching the Super Mario animation in your terminal!
