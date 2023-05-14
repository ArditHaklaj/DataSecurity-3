import tkinter as tk

from tkinter.filedialog import askopenfilename, asksaveasfilename

 

def open_file():

    filepath=askopenfilename(

        filetypes=[("Text Files", ".txt"), ("All Files", ".*")]

    )

    if not filepath:

        return

    txt_edit.delete("1.0", tk.END)

    with open(filepath, "r") as input_file:

        text=input_file.read()

        txt_edit.insert(tk.END, text)

    window.title(f"Simple Text Encrypter - {filepath}")

 

def save_file():

    filepath=asksaveasfilename(

        defaultextension="txt",

        filetypes=[("Text Files", ".txt"), ("All Files", ".*")]

    )

    if not filepath:

        return

    with open(filepath, "w") as output_file:

        text=txt_edit.get("1.0", tk.END)

        output_file.write(text)

    window.title(f"Simple Text Encrypter - {filepath}")

 

def ceasarCypher(message,key,encrypt) -> str: #Remember to remove message

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    output = ""

    message = message.upper()

    for symbol in message:

        if symbol in alphabet:

            num = alphabet.find(symbol) ## Retrieves number associated with the alphabet

            if encrypt == True:

                num = num + key

            else:

                num = num - key

            ## Wrap-around protection

            if num >= len(alphabet):

                num = num - len(alphabet)

            elif num < 0:

                num = num + len(alphabet)

            ## Adding generated letter to translated array

            output = output + alphabet[num]

        else:

            output = output + symbol ## If symbol is not recognised as a letter, it is unaltered

    return output

   def vigenereCypher(message,phrase,encrypt) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    output = ""
    message = message.upper()
    phrase =  phrase.upper()
    for symbol in message:
        if i == len(phrase):
            i = i - len(phrase)
        if symbol in alphabet:
            num = alphabet.find(symbol)
            shiftFactor = alphabet.find(phrase[i])
            if encrypt == True:
                num = num + shiftFactor
            else:
                num = num - shiftFactor
            ## Wrap-around protection
            if num >= len(alphabet):
                num = num - len(alphabet)
            elif num < 0:
                num = num + len(alphabet)
            i = i + 1
            ## Adding generated letter to translated array
            output = output + alphabet[num]
        else:
            output = output + symbol ## If symbol is not recognised as a letter, it is unaltered
    return output

def encrypt():
    cypher=mode.get()
    if cypher == "ceasar":
        key=int(ent_key.get())
        message=txt_edit.get("1.0", tk.END)
        translate=ceasarCypher(message,key,encrypt=True)
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, translate)
    if cypher == "vigenere":
        phrase=str(ent_phrase.get())
        message=txt_edit.get("1.0", tk.END)
        translate=vigenereCypher(message,phrase,encrypt=True)
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, translate)

##Erblini

def decrypt():
    cypher=mode.get()
    if cypher == "ceasar":
        key=int(ent_key.get())
        message=txt_edit.get("1.0", tk.END)
        translate=ceasarCypher(message, key, encrypt=False)
        txt.edit.delete("1.0, tk.END")
        txt_edit.insert(tk.END, translate)
        if cypher == "vigenere":
            phrase=str(ent_phrase.get())
            message = txt_edit.get("1.0", tk.END)
            translate = vigenereCypher(message, phrase, encrypt=False)
            txt_edit.delete("1.0, tk.END")
            txt_edit.insert=(tk.END, translate)

def enable(ent):
    ent.configure(state="normal")
    ent.update()
    def disable(ent):
        ent.configure(state="disabled")
        ent.update()

        
