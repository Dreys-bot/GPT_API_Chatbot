# GPT_API_Chatbot🤖

## System Requirements

You must have Python 3.11 or later installed. Earlier versions of python may not compile.  

When using python 3.10, got the following error message. Need to use python 3.11.  

![Demo](https://github.com/Dreys-bot/GPT_API_Chatbot/blob/main/demo.gif)

---

## Steps to Replicate 

1. Fork this repository and create a codespace in GitHub as I showed you in the youtube video OR Clone it locally.
```
git clone https://github.com/sudarshan-koirala/langchain-openai-chainlit.git
cd GPT_API_Chatbot
```

2. Rename example.env to .env with `cp example.env .env`and input the OpenAI API key as follows. Get OpenAI API key from this [URL](https://platform.openai.com/account/api-keys). You need to create an account in OpenAI webiste if you haven't already.
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

3. Create a virtualenv and activate it
   ```
   python3 -m venv .venv && source .venv/bin/activate
   ```

   If you have python 3.11, then the above command is fine. But, if you have python version less than 3.11. Using conda is easier. First make sure that you have conda installed. Then run the following command.
   ```
   conda create -n .venv python=3.11 -y && source activate .venv
   ```

4. Run the following command in the terminal to install necessary python packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the following command in your terminal to start the chat UI:
   ```
   chainlit run document_qa.py -w
   chainlit run main.py -w
   chainlit run chroma_db_basics.py -w
   chainlit run Youtube_search.py -w
   ```
---
