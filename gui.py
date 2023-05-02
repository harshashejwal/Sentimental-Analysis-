from tkinter import *
from transformers import pipeline

def get_emotion_label():
    text = input_box.get('1.0', END).strip()
    emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')
    label = emotion(text)[0]['label']
    output_label.config(text=f'Emotion Label: {label}')

#  the GUI
root = Tk()
root.geometry("500x300")
root.title('Emotion Detection')

#the input box and label
input_label = Label(root, text='Enter your text:')
input_label.pack()
input_box = Text(root, height=5, width=50)
input_box.pack()

#  the button to trigger the sentiment analysis
analyze_button = Button(root, text='Analyze', command=get_emotion_label)
analyze_button.pack()

#  the output label
output_label = Label(root, text='')
output_label.pack()

# Start the GUI
root.mainloop()
