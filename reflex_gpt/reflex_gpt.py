import reflex as rx

from . import chat, pages, navigation

app = rx.App()
app.add_page(pages.home_page, route=navigation.routes.HOME_ROUTE)
app.add_page(pages.about_page, route=navigation.routes.ABOUT_ROUTE)
app.add_page(chat.chat_page, route=navigation.routes.CHAT_ROUTE)
