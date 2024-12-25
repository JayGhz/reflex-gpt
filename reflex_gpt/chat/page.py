import reflex as rx

from reflex_gpt import ui


def chat_page():
    return ui.base_layout(
        rx.vstack(
            rx.input(
                placeholder="Type a message...",
                width="100%",
                padding="1rem",
                border="none",
                radius="small",
                shadow="md",
            ),
            spacing="0",
            width="100%",
        ),
    )
