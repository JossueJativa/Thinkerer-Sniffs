import customtkinter as ctk

class Custom_Input:
    def __init__(self, bg_color, fg_color, text_color, width, height, border_radius):
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.text_color = text_color
        self.width = width
        self.height = height
        self.border_radius = border_radius

    def create_input(self, parent, textvariable=None, show=None):
        input_widget = ctk.CTkEntry(
            parent,
            placeholder_text="",
            textvariable=textvariable,
            show=show,
            width=self.width,
            height=self.height,
            corner_radius=self.border_radius
        )
        
        # Apply colors
        input_widget.configure(
            fg_color=self.bg_color,
            text_color=self.text_color
        )

        return input_widget