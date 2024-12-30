import reflex as rx

from reflex_gpt import ui

from .state import ChatMessage, ChatState
from .form import chat_form


def message_box(chat_message: ChatMessage):
    return rx.box(
        rx.text(chat_message.message),
        background_color=rx.cond(chat_message.is_bot, rx.color("gray"), rx.color("blue")),
    )


def chat_page():

    return ui.base_layout(
        rx.vstack(
            rx.heading("Chat Here", size="9"),
            rx.box(
                rx.foreach(ChatState.messages, message_box),
                width="100%",
            ),
            chat_form(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
