from tkinter import *
from textblob import TextBlob

positive = 0
neutral = 0
negative = 0
total = 0

def analyze():
    global positive, neutral, negative, total

    if total >= 10:
        result.config(text="10 sentences reached!")
        return

    sentence = entry.get().strip()

    if sentence == "":
        return

    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
        positive += 1
    elif polarity < 0:
        sentiment = "Negative"
        negative += 1
    else:
        sentiment = "Neutral"
        neutral += 1

    total += 1

    polarity_lbl.config(text=f"Polarity Score: {polarity:.2f}")
    result.config(text=f"Latest Result: {sentiment}")

    history.insert(END, f"{sentiment}: {sentence}")

    pos_lbl.config(text=f"Positive: {positive}")
    neu_lbl.config(text=f"Neutral: {neutral}")
    neg_lbl.config(text=f"Negative: {negative}")

    entry.delete(0, END)

def clear_all():
    global positive, neutral, negative, total

    positive = neutral = negative = total = 0

    history.delete(0, END)

    pos_lbl.config(text="Positive: 0")
    neu_lbl.config(text="Neutral: 0")
    neg_lbl.config(text="Negative: 0")

    polarity_lbl.config(text="Polarity Score: 0.00")
    result.config(text="Latest Result: None")

root = Tk()
root.title("Sentiment Dashboard")
root.geometry("600x500")

Label(root,text="SENTIMENT DASHBOARD",
      font=("Arial",16,"bold")).pack(pady=10)

entry = Entry(root,width=50)
entry.pack(pady=5)

Button(root,text="Analyze",
       command=analyze,bg="lightgreen").pack(pady=3)

Button(root,text="Clear All",
       command=clear_all,bg="tomato").pack(pady=3)

polarity_lbl = Label(root,text="Polarity Score: 0.00")
polarity_lbl.pack()

result = Label(root,text="Latest Result: None",
               font=("Arial",11,"bold"))
result.pack(pady=5)

pos_lbl = Label(root,text="Positive: 0",fg="green")
pos_lbl.pack()

neu_lbl = Label(root,text="Neutral: 0",fg="blue")
neu_lbl.pack()

neg_lbl = Label(root,text="Negative: 0",fg="red")
neg_lbl.pack()

Label(root,text="Sentence History").pack(pady=5)

history = Listbox(root,width=70,height=12)
history.pack()

root.mainloop()
