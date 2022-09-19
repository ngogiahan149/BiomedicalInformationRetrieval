
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from tkinter import ttk
from search import searchFunc, advancedSearch
from openFile import *
from textSummarize import *
import spacy

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class mainWindow():
    def __init__(self):
        
        window = Tk()
        window.title("Search Engine")
        window.geometry("1300x800")
        window.configure(bg = "#FFF5E4")

        #set up GUI with canvas
        canvas = Canvas(
            window,
            bg = "#FFF5E4",
            height = 800,
            width = 1300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
       
        canvas.create_rectangle(
            11.0,
            18.0,
            163.0,
            266.0,
            fill="#FFFFFF",
            outline="")
        # Rectangle for file content
       
        frame = Frame(canvas, width = 1000, height = 700, background = "white")
        frame.place(
            x = 191.0,
            y = 68.0,
        )

        global counter_content
        # ADDING A SCROLLBAR
        for widget in frame.winfo_children():
            widget.destroy()

        mycanvas = Canvas(
            frame,
            bg="#FFF5E4",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        mycanvas.pack(side="left", fill="both", expand=True)
        myscrollbar = Scrollbar(frame, orient="vertical", command=mycanvas.yview)
        myscrollbar.pack(side="right", fill="y")

        mycanvas.configure(yscrollcommand=myscrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=(0,0,2000,2000)))

        second_frame = Frame(mycanvas)
        mycanvas.create_window((0, 0), window=second_frame, anchor="nw")

        # canvas.create_window(0, 0, window = frame)
        # scroll_canvas = Canvas(frame)
        # scroll_frame = Frame(scroll_canvas, width = 950, height = 700)
        # scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
        # scroll_frame.bind(
        # "<Configure>",
        # lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        # scroll_canvas.create_window(0,0, window=scroll_frame, anchor='nw')
        # scroll_canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row = 3, column = 3)
        # scroll_canvas.place(relheight=1, relwidth=0.99)
        canvas.create_rectangle(
            190.0,
            25.0,
            514.0,
            53.0,
            fill="#FFFFFF",
            outline="")
        
        
        #Button import XML 
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))   
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command = lambda: display_xml(second_frame, mycanvas),
            relief="flat"
        )
        button_1.place(
            x=35.0,
            y=197.0,
            width=99.0,
            height=31.0
        )
        #Button import JSON file
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_json(second_frame),
            relief="flat"
        )
        button_2.place(
            x=33.0,
            y=129.0,
            width=99.0,
            height=32.0
        )

        canvas.create_text(
            33.0,
            35.0,
            anchor="nw",
            text="Import Data File",
            fill="#000000",
            font=("RobotoRoman Bold", 15 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            369.5,
            39.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_1.place(
            x=247.0,
            y=28.0,
            width=245.0,
            height=20.0
        )


        #Create nlp
        nlp = spacy.load('en_core_web_lg')

        #Button simple search
        button_simpleSearch = Button(
            borderwidth=0,
            highlightthickness=0,
            text = "Simple Search",
            activebackground = '#4F0B21',
            activeforeground = 'white',
            relief="flat",
            background = '#850E35',
            fg = 'white',
            font = ('RobotoRoman Regular', 8, 'bold'),
            command = lambda: searchFunc(second_frame, entry_1.get()),
        )
        button_simpleSearch.place(
            x=550.0,
            y=25.0,
            width=99.0,
            height=32.0
        )
        #button_simpleSearch.configure(command = searchFunc(frame, entry_1.get()))
        #Button Advanced Search
        button_advancedSearch = Button(
            borderwidth=0,
            highlightthickness=0,
            text = "Advanced Search",
            activebackground = '#4F0B21',
            activeforeground = 'white',
            relief="flat",
            background = '#850E35',
            fg = 'white',
            font = ('RobotoRoman Regular', 8, 'bold'),
            command = lambda: advancedSearch(second_frame, entry_1.get(), nlp),
        )
        button_advancedSearch.place(
            x=650.0,
            y=25.0,
            width=99.0,
            height=32.0
        )
        
        

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            210.0,
            39.0,
            image=image_image_1
        )

        canvas.create_text(
            18.0,
            83.0,
            anchor="nw",
            text="Choose option below to import file",
            fill="#000000",
            font=("RobotoRoman Regular", 9 * -1)
        )
        # # Number of sentences
        # canvas.create_text(
        #     33,
        #     400.0,
        #     anchor="nw",
        #     text= count_sentences_xml(),
        #     fill="#EE6983",
        #     font=("RobotoCondensed Bold", 30 * -1),
            
        # )

        # canvas.create_text(
        #     33,
        #     420.0,
        #     anchor="nw",
        #     text="Sentences",
        #     fill="#000000",
        #     font=("RobotoRoman Regular", 14 * -1)
        # )

        # canvas.create_text(
        #     33,
        #     370.0,
        #     anchor="nw",
        #     text="980",
        #     fill="#EE6983",
        #     font=("RobotoCondensed Bold", 30 * -1)
        # )

        # canvas.create_text(
        #     33,
        #     350,
        #     anchor="nw",
        #     text="Words",
        #     fill="#000000",
        #     font=("RobotoRoman Regular", 14 * -1)
        # )

        # canvas.create_text(
        #     33,
        #     300.0,
        #     anchor="nw",
        #     text="1090",
        #     fill="#EE6983",
        #     font=("RobotoCondensed Bold", 30 * -1)
        # )

        # canvas.create_text(
        #     33,
        #     280.0,
        #     anchor="nw",
        #     text="Characters",
        #     fill="#000000",
        #     font=("RobotoRoman Regular", 14 * -1)
        # )
        window.resizable(True, True)
       
        window.mainloop()

mainWindow = mainWindow()