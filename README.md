# Typing Speed Test

This project is a Typing Speed Test application built using Python's `tkinter` and `customtkinter` libraries. The application tests your typing speed and accuracy by providing random texts for you to type within a set time limit.

## Features
- **Random Texts:** The application provides different text passages for each test.
- **Typing Speed Measurement:** Calculates and displays the number of words per minute (WPM).
- **Accuracy Measurement:** Calculates and displays the typing accuracy as a percentage.
- **Retry Option:** Allows the user to retake the test with a new random text.

## Requirements
- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `customtkinter` (can be installed via pip)

## Setup

1. **Install `customtkinter`:**
    ```bash
    pip install customtkinter
    ```

2. **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

3. **Run the Application:**
    ```bash
    python typing_speed_test.py
    ```

## Usage

1. **Start the Application:**
   - Run the script and a window will open.
   
2. **Choose a Text:**
   - The application will randomly select a text for you to type.
   
3. **Start Typing:**
   - Begin typing the displayed text as quickly and accurately as you can.
   
4. **View Results:**
   - After 60 seconds, the test will automatically stop and display your words per minute (WPM) and accuracy percentage.

5. **Retry:**
   - Press the "Retry" button to start a new test with a different text.

## Project Structure
- `typing_speed_test.py`: The main script containing the application logic.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)

Happy typing!
