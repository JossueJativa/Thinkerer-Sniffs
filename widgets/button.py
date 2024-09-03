from customtkinter import CTkButton

class Custom_Button:
    def __init__(self, text, command, fg_color, hover_color):
        self.text = text
        self.command = command
        self.fg_color = fg_color
        self.hover_color = hover_color

    def create_button(self, parent):
        button = CTkButton(
            parent,
            text=self.text,
            command=self.command,
            fg_color=self.fg_color,
            hover_color=self.hover_color
        )

        return button