import reflex as rx

from reflex_gpt import ui 

def about_page() -> rx.Component:
    return ui.base_layout(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("About gpt-reflex", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )