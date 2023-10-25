from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl
import openai
import os

os.environ['OPENAI_API_KEY'] = "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"
openai.api_key = "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"

template = """Question: {question}

Answer: Let's think step by step."""


@cl.on_chat_start
def main():
    # Instantiate the chain for that user session
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

    # Store the chain in the user session
    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message: cl.Message):
    # Retrieve the chain from the user session
    llm_chain = cl.user_session.get("llm_chain")  # type: LLMChain

    # Call the chain asynchronously
    res = await llm_chain.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])

    # Do any post processing here

    # "res" is a Dict. For this chain, we get the response by reading the "text" key.
    # This varies from chain to chain, you should check which key to read.
    await cl.Message(content=res["text"]).send()