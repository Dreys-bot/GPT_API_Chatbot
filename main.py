import chainlit as cl
import openai
import os

os.environ['OPENAI_API_KEY'] = "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"
openai.api_key = "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"

#return everything that the user inputs
model_name = "gpt-3.5-turbo"
settings = {
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}


@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )


@cl.on_message
async def main(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")

    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()