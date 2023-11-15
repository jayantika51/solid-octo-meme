from tkinter import*
import random

root.geometry("300x300")
root.title("color randomizer")
root.config("")

label_name= Label(root, text="",bg="white")
label_name.place(anchor=CENTER)

class game():
    def __init__(self):
        score=0
        self.__score=0
        
    def updateGame(self):
        self.text=["green","orange","yellow","blue","red","black","purple","pink"]
        self.random_number_for_text = random.randint(0,7)
        self.color=["green","orange","yellow","blue","red","black","purple","pink"]
        self.random_number_for_color = random.randint(0,7)
        label_name["text"]= self.text[self.random_number_for_text]
        label_name["fg"]=self.color[self.random_number_for_color]
        
        
        
btn= Button(root, text="START",command=obj.updateGame, bg="dark olive green", fg="white", relief=FLAT, padx=10, pady=1, font=("Arial",15))
root.mainloop()        