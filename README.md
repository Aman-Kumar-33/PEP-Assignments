## Project Purpose

The purpose of this project is to understand how images can be represented and constructed using **ASCII characters** by building them layer by layer through pure logic. Instead of using image-processing libraries or prebuilt tools, this project focuses on manually generating an image using conditional statements and character placement.

This approach helps in:
- Learning how 2D images are represented as rows and columns
- Understanding pixel-to-character mapping
- Practicing control flow (if–elif–else) and nested loops
- Developing a low-level understanding of how rendering works internally
- Improving logical thinking by converting a visual pattern into code

## How the Code Works

The program generates the ASCII image using a row-by-row and column-by-column traversal, similar to how pixels are processed in a real image.

### Core Logic
- The program uses two nested loops:
  - The outer loop iterates over rows (r)
  - The inner loop iterates over columns (c)
- Each position (r, c) represents a single “pixel” in the ASCII image.

### Character Selection
- For every row, a dedicated elif r == X: block is used.
- Inside each row block, the column index c is checked against fixed ranges using if–elif conditions.
- Based on the column range, a specific ASCII character is assigned (such as `-`, `+`, `*`, `#`, `%`, `=`, `'`, `^`, etc.).

Example logic pattern:
- Left part of the row → background characters (e.g., `-`)
- Middle part of the row → image details
- Right part of the row → background characters again

This ensures:
- Each row always has the same width
- The image remains aligned and consistent
- Complex shapes can be formed by gradually changing character ranges across rows

### Line Construction
- Characters are appended one by one to a string (line)
- Once all columns for a row are processed, the line is printed
- Repeating this process for all rows creates the full ASCII image

### Key Design Rules Followed
- No image-processing libraries are used
- Only basic programming constructs are allowed
- The image is built layer by layer, making the logic easy to trace and debug
- Every character on the screen is produced intentionally through code

This structured approach mirrors how real rendering systems work at a very basic level, making the program both educational and visually expressive.

## How to Run the Program

1. Make sure Python is installed on your system.  
   You can check this by running:
   ```bash
   python --version
2. Save the program file (for example): ascii_img.py
3. Open a terminal or command prompt and navigate to the folder containing the file.
4. Run the program using: python ascii_image.py
5. After execution, the generated ASCII image will be saved in a new file named: img.txt
6. Open img.txt using any text editor or view it in the terminal to see the final ASCII image.
   


