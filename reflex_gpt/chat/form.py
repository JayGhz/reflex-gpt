import reflex as rx

from .state import ChatState


def chat_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.text_area(
                name="message",
                placeholder="Type something...",
                required=True,
                width="100%",
            ),
            rx.hstack(
                rx.button("Send", type="submit"),
                rx.cond(
                    ChatState.did_submit,   
                    rx.text("Success"),
                    rx.fragment(),
                )
            ),
        ),
        on_submit=ChatState.handle_submit,
        reset_on_submit=True,
    )
