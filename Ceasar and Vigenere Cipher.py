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
