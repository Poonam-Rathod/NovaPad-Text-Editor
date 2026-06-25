import tkinter as tk
from tkinter import filedialog 
from tkinter import colorchooser

class TextEditor:
    
    def __init__(self):
        
        self.root = tk.Tk()
        
        self.font_size = 14
        
        self.themes = {

          "Tokyo Night": {
          "text_bg": "#1E1E2E",
          "text_fg": "#CDD6F4",
          "line_bg": "#181825",
          "line_fg": "#6C7086",
          "status_bg": "#313244",
          "status_fg": "#CDD6F4",
          "root_bg": "#1E1E2E"
         },

         "Lavender": {
         "text_bg": "#2B213A",
         "text_fg": "#F5EFFF",
         "line_bg": "#1E172A",
         "line_fg": "#B9A7D9",
         "status_bg": "#3A2D52",
         "status_fg": "#FFFFFF",
         "root_bg": "#2B213A"
         },
         
         "Ocean Blue": {
          "text_bg": "#0F172A",
          "text_fg": "#BFDBFE",
          "line_bg": "#1E293B",
          "line_fg": "#64748B",
          "status_bg": "#1E293B",
          "status_fg": "#BFDBFE",
          "root_bg": "#0F172A"
         },

         "Rose Pink": {
          "text_bg": "#2B1E2F",
          "text_fg": "#F5D0FE",
          "line_bg": "#3B2A40",
          "line_fg": "#C084FC",
          "status_bg": "#3B2A40",
          "status_fg": "#F5D0FE",
         "root_bg": "#2B1E2F"
         },

        "Catppuccin": {
         "text_bg": "#1E1E2E",
         "text_fg": "#CDD6F4",
         "line_bg": "#181825",
         "line_fg": "#6C7086",
         "status_bg": "#313244",
         "status_fg": "#CDD6F4",
         "root_bg": "#1E1E2E"
         }

        }
        
        self.setup_window()
        
        self.create_text_area()
        
        self.create_menu()
        
        self.create_status_bar()
        
        self.apply_theme("Tokyo Night")
        
        self.dark_mode = True
        
        self.root.bind("<Control-equal>",self.increase_font)
        
        self.root.bind("<Control-minus>",self.decrease_font)
        
        self.root.mainloop()
        
        
    def setup_window(self):
        self.root.title("NovaPad")
        self.root.geometry("1200x700")
        self.root.configure(bg="#1E1E1E")
    
    def create_text_area(self):
          
        self.editor_frame = tk.Frame(
          self.root,
          bg="#1E1E1E"
)
        self.editor_frame.pack(
            expand=True,
            fill=tk.BOTH
    
        )
         
        self.text = tk.Text(
         self.editor_frame,
         font=("Consolas",self.font_size),
         wrap=tk.WORD,
         bg="#1E1E1E",
         fg="#D4D4D4",
         insertbackground="white",
         undo=True,
         borderwidth=0
        )
        self.text.pack(
         side=tk.LEFT,
         expand=True,
         fill=tk.BOTH
        )
        
        self.text.bind(
            "<KeyRelease>",
            self.on_key_release
        )
        
        self.line_numbers = tk.Text(
            self.editor_frame,
            width=4,
            font=("Consolas",self.font_size),
            bg="#252526",
            fg="#858585",
            state="disabled"
            
        )
        
        self.line_numbers.pack(
             side=tk.LEFT,
            fill=tk.Y
        )
        
       
        
    def key_pressed(self,event):
         print(event.keysym)
            
        
         
    def increase_font(self,event=None):
        print("Increased clicked")
        self.font_size +=1
        
        self.text.config(
            font=("Consolas",self.font_size)
        ) 
        
        self.line_numbers.config(
            font=("Consolas",self.font_size)
        ) 
        
    def decrease_font(self,event=None):
        
        if self.font_size > 8:
            self.font_size -=1
            
            self.text.config(
            font=("Consolas",self.font_size)
        ) 
        
            self.line_numbers.config(
            font=("Consolas",self.font_size)
        ) 
            
        
    def on_key_release(self,event=None):
        
        self.update_status()
        
        self.update_line_numbers()  
    
    def update_line_numbers(self):
        line_count= self.text.index("end-1c").split(".")[0]
        
        numbers = "\n".join(
            str(i)
            for i in range(1,int(line_count) +1)
        )   
        
        self.line_numbers.config(state="normal")
        
        self.line_numbers.delete(1.0,tk.END)
        
        self.line_numbers.insert(1.0,numbers)
        
        self.line_numbers.config(state="disabled") 
    
    def create_status_bar(self):
        self.status_bar=tk.Label(
            self.root,
            text="Words:0 | Characters:0",
            anchor ="w",
            padx=15,
            pady=5,
            bd=1,
            bg="#181825",
            fg="#CDD6F4",
            relief="solid"
        )   
        
        self.status_bar.pack(
            side=tk.BOTTOM,
            fill=tk.X
        ) 
    
    def update_status(self,event=None):
        content = self.text.get(1.0,tk.END)
        
        words = len(content.split())
        
        chars = len(content) -1
        
        self.status_bar.config(
            text= f"Words: {words} | Characters: {chars}"
        )
        
         
    def create_menu(self):

      self.menu = tk.Menu(self.root)

      self.root.config(menu=self.menu)

      self.file_menu = tk.Menu(
         self.menu,
         tearoff=0
    )

      self.menu.add_cascade(
        label="File",
        menu=self.file_menu
    )
      
      self.edit_menu = tk.Menu(
          self.menu,
          tearoff=0
      )
      
      self.menu.add_cascade(
          label="Edit",
          menu=self.edit_menu
      )
      
      self.edit_menu.add_command(
          label="Find & Replace",
          command=self.open_find_replace
      )
      

      self.file_menu.add_command(label="New",command=self.new_file)

      self.file_menu.add_command(label="Open",command=self.open_file)

      self.file_menu.add_command(label="Save",command=self.save_file)
 
      self.file_menu.add_separator()
      
    #   self.menu.add_command(label="toggle Theme",command=self.toggle_theme)
 
      self.file_menu.add_command(label="Exit",command=self.exit_app)
      
      self.edit_menu.add_separator()
      
      self.edit_menu.add_command(
          label="Increase Font",
          command = self.increase_font
      )
      
      self.edit_menu.add_command(
          label="Decrease Font",
          command=self.decrease_font
      )
      
      self.theme_menu=tk.Menu(
          self.menu,
          tearoff=0
      )
      
      self.menu.add_cascade(
          label="Themes",
          menu=self.theme_menu
      )
      
      self.theme_menu.add_command(
          label="Tokyo Night",
          command= lambda: self.apply_theme("Tokyo Night")
      )
      
      self.theme_menu.add_command(
          label="Catppuccin",
          command= lambda:self.apply_theme("Catppuccin")
      )
      
      self.theme_menu.add_command(
          label="Ocean Blue",
         command=lambda: self.apply_theme("Ocean Blue")
      )

      self.theme_menu.add_command(
          label="Rose Pink",
          command=lambda: self.apply_theme("Rose Pink")
      )
      
      self.theme_menu.add_separator()
      
      self.theme_menu.add_command(
          label="Custom Theme",
          command=self.create_custom_theme
      )
      
      self.font_menu = tk.Menu(self.menu, tearoff=0)
      
      self.menu.add_cascade(
          label="Fonts",
          menu=self.font_menu
      )
      
      self.font_menu.add_command(
          label="Consolas",
          command = lambda:self.change_font("Consolas")
      )
      
      self.font_menu.add_command(
          label="Arial",
          command = lambda:self.change_font("Arial")
      )
      
      self.font_menu.add_command(
          label="JetBrains Mono",
          command = lambda:self.change_font("JetBrains Mono")
      )
      
      self.font_menu.add_command(
          label="Fira Code",
          command = lambda:self.change_font("Fira Code")
      )
      
      self.font_menu.add_command(
          label="Courier New",
          command = lambda:self.change_font("Courier New")
      )
      
      self.font_menu.add_command(
          label="Helvetica",
          command = lambda:self.change_font("Helvetica")
      )
      
      self.font_menu.add_command(
          label="Times New Roman",
          command = lambda:self.change_font("Times New Roman")
      )
      
      self.font_menu.add_command(
          label="Verdana",
          command = lambda:self.change_font("Verdana")
      )
      
      self.font_menu.add_command(
          label="Georgia",
          command = lambda:self.change_font("Georgia")
      )
      
      self.font_menu.add_command(
          label="DejaVu Sans Mono",
          command = lambda:self.change_font("DejaVu Sans Mono")
      )
      
      self.font_menu.add_command(
          label="Trebuchet MS",
          command = lambda:self.change_font("Trebuchet MS")
      )
      
    
      
      
    
    
    def open_find_replace(self):
        self.find_window= tk.Toplevel(self.root)
        
        self. find_window.title("Find &s Replace")
        
        self. find_window.geometry("300x150")
        
        tk.Label(
            self.find_window,
            text="Find:"
        ).pack()
        
        tk.Label(
           self.find_window,
           text="Replace:"
        ).pack()
        
        self.find_entry= tk.Entry(self.find_window)
        self.find_entry.pack()
        
        self.replace_entry = tk.Entry(self.find_window)
        self.replace_entry.pack()
        
        tk.Button(
            self.find_window,
            text="Replace All",
            command=self.replace_text
            
        ).pack(pady=5)
           
        
    def replace_text(self):
        
        self. find = self.find_entry.get()
        
        self.replace= self.replace_entry.get()
        
        self.content = self.text.get(1.0,tk.END)
        
        self.content= self.content.replace(self.find,self.replace)
        
        self.text.delete(1.0,tk.END)
        
        self.text.insert(tk.END,self.content)
        
        
        
    def new_file(self):
        self.text.delete(1.0,tk.END)
    
    def open_file(self):
       file_path= filedialog.askopenfilename()
       if file_path:
          self.text.delete(1.0,tk.END)
          with open(file_path,"r") as file:
              
              self.text.insert(
                  tk.END,
                  file.read()
              )
            

             
        
    def save_file(self):
        file_path= filedialog.asksaveasfilename()
        if file_path:
            self.text.get(1.0,tk.END)
            with open (file_path,"w") as file:
             file.write(
                self.text.get(1.0,tk.END)
            )
    
    def exit_app(self):
        self.root.destroy() 
    
    # def toggle_theme(self):
        
    #     if self.dark_mode:
    #         self.root.configure(bg="#F8F4FF")
            
    #         self.text.config(
    #             bg="#EDE4FF",
    #             fg="#2B213A",
    #             insertbackground="black"
    #         )    
            
    #         self.dark_mode= False    
        
    #     else:
    #         self.root.configure(bg="#2B213A") 
            
    #         self.text.config(
    #             bg="#1E1E1E",
    #             fg="#D4D4D4",
    #             insertbackground="white"
    #         )  
            
    #         self.dark_mode = True  
    
    def apply_theme(self,theme_name):
        theme = self.themes[theme_name]
        
        self.root.configure(
            bg=theme["root_bg"]
        )
        
        self.text.config(
           padx=20,
           pady=20
        )
        
        self.text.config(
            bg= theme["text_bg"],
            fg= theme["text_fg"]
        )
        
        self.line_numbers.config(
           state="normal" 
        )
        
        self.line_numbers.config(
            bg=theme["line_bg"],
            fg=theme["line_fg"]
        )
        
        self.line_numbers.config(
            state="disabled"
        )
        
        self.status_bar.config(
            bg=theme["status_bg"],
            fg=theme["status_fg"]
        )
        
    def create_custom_theme(self):
        
        text_bg = colorchooser.askcolor(
            title="Choose Text Background"
        )[1]
        
        if not text_bg:
            return
        
        text_fg = colorchooser.askcolor(
            title = "Choose Text Color"
        )[1]
        
        if not text_fg:
            return
        
        self.text.config(
            bg=text_bg,
            fg=text_fg,
            insertbackground=text_fg
            
        ) 
        
        self.line_numbers.config(
           state="normal",
           bg=text_bg,
           fg=text_fg
        )

        self.line_numbers.config(
          state="disabled"
        )

        self.status_bar.config(
          bg=text_bg,
          fg=text_fg
        )

        self.root.configure(
          bg=text_bg
        )
        
    def change_font(self,font_name):
        self.text.config(
            font=(font_name,self.font_size)
        )  
        
        self.line_numbers.config(
            font=(font_name,self.font_size)
        )     
                
            
        
editor =TextEditor()        