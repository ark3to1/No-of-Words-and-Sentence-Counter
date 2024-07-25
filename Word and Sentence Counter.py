from tkinter import *

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    # Simple assumption: split by period ('.') and count.
    sentences = text.split('.')
    return len(sentences)


def count():
    input_text = text_box.get("1.0", END)
    num_words = count_words(input_text)
    num_sentences = count_sentences(input_text)
    result.config(text=f"Words = {num_words}\nSentences = {num_sentences-1}")

#----------------------------------------------------------------- (Front End)-----------------------------------------------------------------

root = Tk()

root.title("Words & Sentence Counter")
root.geometry("500x500+450+100")
root.resizable(False, False)

heading1 = Label(root, text='  Welcome to "Word and Sentence Counter"  ', font=('Times New Roman', 18, "bold"), bd=5, relief="ridge", fg="red")
heading1.pack(pady=30)

heading2 = Label(root, text='Type your text in below text-box', font=('Calibri', 15, "bold"))
heading2.pack()

text_box = Text(root, font=('arial', 10), bg='sky blue')
text_box.place(x=25, y=140, relwidth=0.9, relheight=0.3)

count_button = Button(root, text="Count", font=('arial', 15, 'bold'), bg='grey', fg='black', bd='5', command=count)
count_button.pack(pady=170)

result = Label(root, text="", font=("Arial", 20, 'bold'), fg='red')
result.place(x=150, y=350)

root.mainloop()


