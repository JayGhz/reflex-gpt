import reflex as rx
from .sidebar import base_sidebar


def base_layout(*args, **kwargs) -> rx.Component:
    return rx.container(
        base_sidebar(),
        rx.fragment(
            *args,
            **kwargs,
        ),
    )
