
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from openFile import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class mainWindow():
    def __init__(self):
        
        window = Tk()

        window.geometry("661x324")
        window.configure(bg = "#FFF5E4")

        #set up GUI with canvas
        canvas = Canvas(
            window,
            bg = "#FFF5E4",
            height = 324,
            width = 661,
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
        canvas.create_rectangle(
            
            191.0,
            68.0,
            518.0,
            235.0,
            fill="#FFFFFF",
            outline="")
        
        frame = Frame(window, width = 518, height = 235)
        frame.pack()
        frame.place(
            x = 191.0,
            y = 68.0,
        )
        canvas.grid(row = 1, column = 1)
        # label1 = Label(frame, text = "Hello Worldsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssss")      
        # label1.grid(row = 2, column = 1)
        # label2 = Label(frame, text = "Hello Worldsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssss")      
        # label2.grid(row = 2, column = 2)
        cols=['Col1','Col2','Col3']
        data = [ ["val1", "val2", "val3"],
                ["asd1", "asd2", "asd3"],
                ["bbb1", "bbb3", "bbb4"],
                ["ccc1", "ccc3", "ccc4"],
                ["ddd1", "ddd3", "ddd4"],
                ["eee1", "eee3", "eee4"] ]
        for y in range(len(data)+1):
            for x in range(len(cols)):
                if y==0:
                    e=Label(frame, font=("RobotoRoman Regular", 9 * -1),bg='light blue',justify='center', text = cols[x])
                    e.grid(column=x, row=y)
                    # e.insert(0,cols[x])
                else:
                    e=Label(frame, text = data[y-1][x])
                    e.grid(column=x, row=y)
                                     
        

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
            command = lambda: open_xml(),
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
            command=lambda: open_json(),
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

        canvas.create_text(
            438.0,
            274.0,
            anchor="nw",
            text="50",
            fill="#EE6983",
            font=("RobotoCondensed Bold", 30 * -1),
            
        )

        canvas.create_text(
            437.0,
            253.0,
            anchor="nw",
            text="Sentences",
            fill="#000000",
            font=("RobotoRoman Regular", 14 * -1)
        )

        canvas.create_text(
            325.0,
            274.0,
            anchor="nw",
            text="980",
            fill="#EE6983",
            font=("RobotoCondensed Bold", 30 * -1)
        )

        canvas.create_text(
            328.0,
            253.0,
            anchor="nw",
            text="Words",
            fill="#000000",
            font=("RobotoRoman Regular", 14 * -1)
        )

        canvas.create_text(
            211.0,
            274.0,
            anchor="nw",
            text="1090",
            fill="#EE6983",
            font=("RobotoCondensed Bold", 30 * -1)
        )

        canvas.create_text(
            210.0,
            253.0,
            anchor="nw",
            text="Characters",
            fill="#000000",
            font=("RobotoRoman Regular", 14 * -1)
        )
        window.resizable(False, False)
        window.mainloop()

mainWindow = mainWindow()