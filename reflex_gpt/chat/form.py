import reflex as rx

from .state import ChatState


def chat_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.text_area(
                name="message",
                placeholder="Type something ...",
                padding="1rem",
                required=True,
                width="100%",
                border_radius="8px",
                height="5px",
                background_color="transparent",
            ),
            rx.hstack(
                rx.button("Send", type="submit", border_radius="8px"),
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
