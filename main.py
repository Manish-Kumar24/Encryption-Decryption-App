import tkinter as tk
from tkinter import messagebox
from tkinter import font
from encrypt_decrypt import encrypt_message, decrypt_message, generate_key

def generate_key_and_display():
    key = generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key.decode())

def encrypt():
    key = key_entry.get()
    message = message_entry.get()
    if not key or not message:
        messagebox.showwarning("Input Error", "Key and message cannot be empty!")
        return
    try:
        encrypted_message = encrypt_message(key.encode(), message)
        output_entry.delete(0, tk.END)
        output_entry.insert(0, encrypted_message.decode())
    except Exception as e:
        messagebox.showerror("Encryption Error", str(e))

def decrypt():
    key = key_entry.get()
    encrypted_message = output_entry.get()
    if not key or not encrypted_message:
        messagebox.showwarning("Input Error", "Key and encrypted message cannot be empty!")
        return
    try:
        decrypted_message = decrypt_message(key.encode(), encrypted_message.encode())
        output_entry.delete(0, tk.END)
        output_entry.insert(0, decrypted_message)
    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))

# GUI setup
root = tk.Tk()
root.title("CrypticMessenger")

# Set custom fonts
title_font = font.Font(family='Helvetica', size=18, weight='bold')
label_font = font.Font(family='Helvetica', size=12)
entry_font = font.Font(family='Helvetica', size=10)
button_font = font.Font(family='Helvetica', size=10, weight='bold')

# Set colors
bg_color = "#f0f0f0"
frame_color = "#dcdcdc"
button_color = "#4caf50"
button_text_color = "#ffffff"

root.configure(bg=bg_color)

# Centering the window
window_width = 500
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Title
title_label = tk.Label(root, text="CrypticMessenger", font=title_font, bg=bg_color)
title_label.pack(pady=10)

# Key Frame
key_frame = tk.Frame(root, bg=frame_color, padx=10, pady=10)
key_frame.pack(pady=5, fill='x', padx=10)

tk.Label(key_frame, text="Key:", font=label_font, bg=frame_color).grid(row=0, column=0, sticky='e')
key_entry = tk.Entry(key_frame, width=50, font=entry_font)
key_entry.grid(row=0, column=1, padx=5)
tk.Button(key_frame, text="Generate Key", command=generate_key_and_display, bg=button_color, fg=button_text_color, font=button_font).grid(row=0, column=2, padx=5)

# Message Frame
message_frame = tk.Frame(root, bg=frame_color, padx=10, pady=10)
message_frame.pack(pady=5, fill='x', padx=10)

tk.Label(message_frame, text="Message:", font=label_font, bg=frame_color).grid(row=0, column=0, sticky='e')
message_entry = tk.Entry(message_frame, width=50, font=entry_font)
message_entry.grid(row=0, column=1, padx=5)

# Output Frame
output_frame = tk.Frame(root, bg=frame_color, padx=10, pady=10)
output_frame.pack(pady=5, fill='x', padx=10)

tk.Label(output_frame, text="Output:", font=label_font, bg=frame_color).grid(row=0, column=0, sticky='e')
output_entry = tk.Entry(output_frame, width=50, font=entry_font)
output_entry.grid(row=0, column=1, padx=5)

# Buttons Frame
buttons_frame = tk.Frame(root, bg=bg_color, padx=10, pady=10)
buttons_frame.pack(pady=10)

tk.Button(buttons_frame, text="Encrypt", command=encrypt, bg=button_color, fg=button_text_color, font=button_font).grid(row=0, column=0, padx=10)
tk.Button(buttons_frame, text="Decrypt", command=decrypt, bg=button_color, fg=button_text_color, font=button_font).grid(row=0, column=1, padx=10)

# Center the frames within the root window
title_label.pack(anchor="center")
key_frame.pack(anchor="center")
message_frame.pack(anchor="center")
output_frame.pack(anchor="center")
buttons_frame.pack(anchor="center")

root.mainloop()
