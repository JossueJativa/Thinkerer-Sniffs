import customtkinter as ctk

class Custom_Label:
    def __init__(self, text_color, font):
        self.text_color = text_color
        self.font = font

    def create_label(self, parent, text):
        label = ctk.CTkLabel(
            parent, 
            text=text, 
            font=("Arial", self.font),
            text_color=self.text_color,
            corner_radius=5
        )

        return label
