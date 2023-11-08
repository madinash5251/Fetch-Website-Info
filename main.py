import tkinter as tk
from app.functions import fetch_and_display_info  # Adjust the import path

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Web Content Fetcher")

    # Create and configure GUI components
    url_label = tk.Label(window, text="Enter URL:")
    url_label.pack()

    url_entry = tk.Entry(window, width=50)
    url_entry.pack()

    fetch_button = tk.Button(window, text="Fetch Content", command=lambda: fetch_and_display_info(url_entry.get(), title_label, content_label, image_count_label))
    fetch_button.pack()

    title_label = tk.Label(window, text="Title:")
    title_label.pack()

    content_label = tk.Label(window, text="First 200 chars:")
    content_label.pack()

    image_count_label = tk.Label(window, text="Image Count:")
    image_count_label.pack()

    # Start the main event loop
    window.mainloop()

if __name__ == "__main__":
    main()
