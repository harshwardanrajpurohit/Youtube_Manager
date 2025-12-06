# Youtube_Manager
A simple command-line interface (CLI) application built with Python to manage a personal list of Youtube videos. It utilizes JSON file handling for persistent data update, and delete video entries (name and duration).
# 💡 Simple Python YouTube Manager (CLI)

This is a **basic command-line application** built with Python. It acts like a simple organizer where you can keep track of your favorite YouTube videos by their name and duration.

The goal of this project was to practice **fundamental Python programming** concepts like functions, input/output, and working with local files.

---

## 💾 How It Works (The Simple Breakdown)

| Code Function | What It Does (In Simple Terms) | Python Concept Used |
| :--- | :--- | :--- |
| `load_data()` | **Loads the list** of videos when the app starts. It looks for a file called `youtube.txt`. If the file isn't there, it just starts with an empty list. | `try...except` and JSON reading |
| `save_data_helper()` | **Saves the current list** of videos to the `youtube.txt` file whenever you make a change (add, update, or delete). | JSON writing |
| `list_all_videos()` | **Shows you the list** of all saved videos, numbered from 1. | `for` loop and `enumerate` |
| `add_video()` | **Asks you for the name and time** of a new video and adds it to the list, then saves the list. | User `input()` |
| `update_video()` | **Lets you change** the name or time of an existing video in the list. | List indexing |
| `delete_video()` | **Removes** a video entry from the list. | `del` keyword |
| `main()` | **Runs the whole app!** It shows the main menu and uses a `while True` loop to keep the menu running until you choose the 'Exit' option. | `while` loop and `match` statement |

---

## 🚀 How to Run the App

1.  **Save the Code:** Save the Python code as a file (e.g., `youtube_manager.py`).
2.  **Open Terminal:** Open your terminal or command prompt and navigate to the folder where you saved the file.
3.  **Run the Script:** Type the following command and press Enter:

    ```bash
    python youtube_manager.py
    ```

4.  **Choose Options:** Follow the on-screen menu to list, add, update, or delete your video entries!

---

## ⚙️ Technologies Used

* **Python:** The core programming language.
* **JSON (`import json`):** Used to easily save and load the video data to and from the `youtube.txt` file, ensuring your data is kept between sessions.
