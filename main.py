import tkinter
import customtkinter as ctk
from random import choice


window = ctk.CTk()
window.title("Typing speed test")

# PC Screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# Center coordinates of screen
center_x = int(screen_width/2 - 250)
center_y = int(screen_height/2 - 300)
# Set position in center of screen
window.geometry(f"500x250+{center_x}+{center_y}")
ctk.set_appearance_mode("dark")

correct_press = 0
incorrect_press = 0

def writing_labels():
    # Text List
    text_list = [
        "Miles was an adventurous fox who loved to explore the world. He loved to go on hikes, climbing up trees,"
        " and jumping over fences. One day, while he was out exploring, he came across a wide open field. He was"
        " so excited to explore it, but little did he know, he was not alone. Suddenly, he heard a loud clucking"
        " noise. He turned around and saw a large chicken coming right towards him. It seemed to be chasing him!"
        " Miles was so scared that he started to run. He ran as fast as he could, jumping over fences and ducking"
        " under branches. He was so quick and agile that the chicken couldn't keep up. Miles eventually managed to"
        " escape the chicken, but he was so exhausted from the chase. He collapsed in a nearby bush and took a"
        " well-deserved rest. After a few minutes, Miles got up and continued exploring the world. "
        "He never forgot that day and the chicken that chased him. He was more careful when he explored"
        " the world, but he never stopped jumping over fences and exploring.",
        "Once upon a time, there was a chicken named Cluck who had a dream of one day being able to fly."
        " Every day, Cluck ran and jumped and flapped her wings, determined to reach the sky. One day, after a "
        "particularly long and hard practice, she finally felt ready. She spread her wings and with all her"
        " strength, she jumped and soared into the air. But to her dismay, her wings weren't strong enough to "
        "keep her afloat. She began to fall, and soon found herself plummeting towards a deep fryer. With a loud"
        " sizzle, Cluck was submerged in the hot oil. After a few moments of struggling, she was pulled out by"
        " the local farmer. The farmer was shocked at what he had found. To his amazement, the chicken had been"
        " cooked to perfection. He decided to start a restaurant and serve the fried chicken to his customers. "
        "Soon, the restaurant was a hit. Everyone loved the fried chicken that Cluck had unknowingly prepared. It"
        " wasn't until much later that the farmer realized what he had stumbled upon. He named his restaurant"
        "after the chicken that started it all - Cluck's Fried Chicken, or KFC for short. "
        "And that's how we got KFC."]

    # Choosing one
    text = choice(text_list)

    # split point
    split_point = 0

    # Written text
    global label_left
    label_left = ctk.CTkLabel(window, text=text[0:split_point], fg_color=("#dbdbdb", "#2b2b2b"))
    label_left.place(relx=0.5, rely=0.5, anchor=tkinter.E)

    # Text to write
    global label_right
    label_right = ctk.CTkLabel(window, text=text[split_point:])
    label_right.place(relx=0.5, rely=0.5, anchor=tkinter.W)

    # Letter to press
    global current_letter_label
    current_letter_label = ctk.CTkLabel(window, text=text[split_point],
                                        width=20,
                                        fg_color=("#dbdbdb", "#2b2b2b"),
                                        corner_radius=8)
    current_letter_label.place(relx=0.5, rely=0.6, anchor=tkinter.N)

    # time has gone by
    global time_left_label
    time_left_label = ctk.CTkLabel(window, text=f'0 Seconds', )
    time_left_label.place(relx=0.5, rely=0.4, anchor=tkinter.S)

    global write_able
    write_able = True
    window.bind('<Key>', key_press)

    global passed_seconds
    passed_seconds = 0

    # Binding callbacks to functions after a certain amount of time.
    window.after(60000, stop_test)
    window.after(1000, add_second)


def stop_test():
    global write_able
    write_able = False

    # Calculate the amounts of words
    amount_words = len(label_left.cget("text").split(" "))

    time_left_label.destroy()
    current_letter_label.destroy()
    label_right.destroy()
    label_left.destroy()

    global result_label
    result_label = ctk.CTkLabel(window, text=f'Words per minute: {amount_words}')
    result_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    global precision_label
    precision = correct_press / (correct_press + incorrect_press) * 100
    precision_label = ctk.CTkLabel(window, text=f'precision: {precision:.2f}%')
    precision_label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    # Display a button to restart the game
    global result_button
    result_button = ctk.CTkButton(window, text=f'Retry', command=restart)
    result_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


def restart():
    # Destroy result widgets
    result_label.destroy()
    result_button.destroy()
    precision_label.destroy()

    # re-setup writing labels.
    writing_labels()


def add_second():
    # Add a second to the counter.

    global passed_seconds
    passed_seconds += 1
    time_left_label.configure(text=f'{passed_seconds} Seconds')

    # call this function again after one second if the time is not over.
    if write_able:
        window.after(1000, add_second)


def key_press(event=None):
    global correct_press, incorrect_press
    if event.char.lower() == label_right.cget('text')[0].lower():
        correct_press += 1
        # Deleting one from the right side.
        label_right.configure(text=label_right.cget('text')[1:])
        # Deleting one from the right side.
        label_left.configure(text=label_left.cget('text') + event.char)
        # set the next Letter Label
        current_letter_label.configure(text=label_right.cget('text')[0])
    else:
        incorrect_press += 1


# run
writing_labels()

window.mainloop()
