import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


def select_image(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)


def select_output(entry):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg *.jpeg"), ("All files", "*.*")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)


def watermark_photo(input_image_path, output_image_path, watermark_image_path, position, scale=0.1):
    try:
        base_image = Image.open(input_image_path).convert("RGBA")
        watermark = Image.open(watermark_image_path).convert("RGBA")

        base_width, base_height = base_image.size
        watermark_width, watermark_height = watermark.size

        new_width = int(base_width * scale)
        new_height = int((new_width / watermark_width) * watermark_height)
        watermark = watermark.resize((new_width, new_height), Image.Resampling.LANCZOS)

        base_image.paste(watermark, position, mask=watermark)

        base_image.show()
        base_image.save(output_image_path)

        messagebox.showinfo("Success", f"Watermarked image saved as {output_image_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save watermarked image: {e}")


def add_watermark():
    input_image_path = input_entry.get()
    watermark_image_path = watermark_entry.get()
    output_image_path = output_entry.get()
    scale = float(scale_entry.get())

    watermark_photo(input_image_path, output_image_path, watermark_image_path, (0, 0), scale)


app = tk.Tk()
app.title("Watermark Adder")

tk.Label(app, text="Input Image:").grid(row=0, column=0, padx=10, pady=5)
input_entry = tk.Entry(app, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(app, text="Browse", command=lambda: select_image(input_entry)).grid(row=0, column=2, padx=10, pady=5)

tk.Label(app, text="Watermark Image:").grid(row=1, column=0, padx=10, pady=5)
watermark_entry = tk.Entry(app, width=50)
watermark_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(app, text="Browse", command=lambda: select_image(watermark_entry)).grid(row=1, column=2, padx=10, pady=5)

tk.Label(app, text="Output Image:").grid(row=2, column=0, padx=10, pady=5)
output_entry = tk.Entry(app, width=50)
output_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Button(app, text="Browse", command=lambda: select_output(output_entry)).grid(row=2, column=2, padx=10, pady=5)

tk.Label(app, text="Scale (0-1):").grid(row=3, column=0, padx=10, pady=5)
scale_entry = tk.Entry(app, width=50)
scale_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Button(app, text="Add Watermark", command=add_watermark).grid(row=4, column=1, padx=10, pady=20)

app.mainloop()
