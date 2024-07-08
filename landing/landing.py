"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from os import link
from turtle import width
import reflex as rx
from sqlalchemy import true

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    
    return rx.container(
        rx.hstack(
            rx.image(src="wordmark.svg", width="150px", height="auto"),
            rx.spacer(),    
            rx.hstack(
                rx.link("Github", href="https://github.com/spawnpointlabs"),
                rx.link("Twitter", href="https://twitter.com/spawnpoint_labs"),
                align="center",
                padding="1em"
            ),
            align="center"
        )
        

    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="purple"
    )
)
app.add_page(index) 
