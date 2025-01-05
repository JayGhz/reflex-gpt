from typing import List
import asyncio
import reflex as rx


class ChatMessage(rx.Base):
    message: str
    is_bot: bool


class ChatState(rx.State):
    did_submit: bool = False
    messages: List[ChatMessage] = []

    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit

    def append_message(self, message, is_bot=False):
        self.messages.append(ChatMessage(is_bot=is_bot, message=message))
        
    def get_gpt_messages(self):
        gpt_messages = []
        for chat_message in self.messages:
            role = "user"
            if chat_message.is_bot:
                role = "system"
            gpt_messages.append({
                "role": role,
                "message": chat_message.message
            })
        return

    async def handle_submit(self, form_data: dict):
        print(form_data)
        user_message = form_data.get("message", "")
        if user_message:
            self.did_submit = True
            self.append_message(user_message, is_bot=False)
            yield
            await asyncio.sleep(2)
            self.did_submit = False
            self.append_message(user_message, is_bot=True)
            yield
