import tkinter as tk

# ---------------- DATASETS ---------------- #

happy_words = [
    "happy", "joy", "cheerful", "good", "great",
    "excellent", "love", "smile", "fantastic",
    "wonderful", "delight"
]

sad_words = [
    "sad", "sorrow", "depressed", "bad", "terrible",
    "awful", "hate", "cry", "miserable",
    "tragic", "grief", "disappointed"
]

# ---------------- FUNCTIONS ---------------- #

def number_happy(sentence):
    count = 0

    for word in sentence.lower().split():
        word = word.strip(".,!?;:")
        if word in happy_words:
            count += 1

    return count


def number_sad(sentence):
    count = 0

    for word in sentence.lower().split():
        word = word.strip(".,!?;:")
        if word in sad_words:
            count += 1

    return count


def analyze_tone():

    sentence = entry.get().strip()

    if sentence == "":
        result_label.config(
            text="Please enter a sentence."
        )
        return

    happy_count = number_happy(sentence)
    sad_count = number_sad(sentence)

    if happy_count > sad_count:
        tone = "POSITIVE (HAPPY)"
        color = "green"

    elif sad_count > happy_count:
        tone = "NEGATIVE (SAD)"
        color = "red"

    else:
        tone = "NEUTRAL"
        color = "blue"

    result_label.config(
        text=f"Happy Words: {happy_count}\n\n"
             f"Sad Words: {sad_count}\n\n"
             f"Analysis: {tone}",
        fg=color
    )

    history.insert(
        tk.END,
        f"Happy:{happy_count} | Sad:{sad_count} | {tone}"
    )

    entry.delete(0, tk.END)


def clear_all():

    entry.delete(0, tk.END)

    result_label.config(
        text="Analyze a sentence to see results.",
        fg="black"
    )

    history.delete(0, tk.END)


# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Sentence Tone Analyzer")

# Maximized Window
root.state("zoomed")

root.configure(bg="#ECECEC")

# ---------------- HEADER ---------------- #

title = tk.Label(
    root,
    text="SENTENCE TONE ANALYZER",
    font=("Arial", 26, "bold"),
    bg="#ECECEC"
)

title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Analyze the happiness and sadness level of a sentence",
    font=("Arial", 11),
    bg="#ECECEC"
)

subtitle.pack()

# ---------------- INPUT FRAME ---------------- #

input_frame = tk.Frame(
    root,
    bg="#ECECEC"
)

input_frame.pack(pady=20)

entry = tk.Entry(
    input_frame,
    width=70,
    font=("Arial", 14)
)

entry.pack(pady=10)

button_frame = tk.Frame(
    input_frame,
    bg="#ECECEC"
)

button_frame.pack()

analyze_btn = tk.Button(
    button_frame,
    text="Analyze Tone",
    width=18,
    font=("Arial", 11, "bold"),
    bg="lightgreen",
    command=analyze_tone
)

analyze_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Reset",
    width=18,
    font=("Arial", 11, "bold"),
    bg="tomato",
    command=clear_all
)

clear_btn.grid(row=0, column=1, padx=10)

# ---------------- RESULT FRAME ---------------- #

result_frame = tk.LabelFrame(
    root,
    text="Analysis Result",
    font=("Arial", 14, "bold"),
    padx=20,
    pady=20
)

result_frame.pack(
    fill="x",
    padx=50,
    pady=20
)

result_label = tk.Label(
    result_frame,
    text="Analyze a sentence to see results.",
    font=("Arial", 16, "bold")
)

result_label.pack()

# ---------------- HISTORY FRAME ---------------- #

history_frame = tk.LabelFrame(
    root,
    text="Analysis History",
    font=("Arial", 14, "bold")
)

history_frame.pack(
    fill="both",
    expand=True,
    padx=50,
    pady=20
)

scrollbar = tk.Scrollbar(
    history_frame
)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)

history = tk.Listbox(
    history_frame,
    font=("Arial", 12),
    yscrollcommand=scrollbar.set
)

history.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

scrollbar.config(
    command=history.yview
)

root.mainloop()