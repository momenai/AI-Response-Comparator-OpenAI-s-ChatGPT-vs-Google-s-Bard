import streamlit as st
from answer_generator import generate_answer, get_bard_answer
label_visibility='collapse'

st.title(":green[ChatGPT] vs :blue[Google Bard]")
# st.header("Enter your prompt below:")

message = st.text_input("")

if message:
    chatgpt_answer = generate_answer(message)
    bard_answer = get_bard_answer(message)
    print(bard_answer)
    print("OpenAI", chatgpt_answer)

    col1, col2 = st.columns(2)

    with col1:
        st.header("OpenAI")
        st.markdown(chatgpt_answer)

    with col2:
        st.header("Bard")
        st.markdown(bard_answer)

# from bardapi import Bard
# import openai
# import os
# import streamlit as st


# # ctrl + shift + i, PSID
# os.environ["_BARD_API_KEY"] = "."
# openai.api_key = "sk"


# def generate_answer(text):
#     prompt = ""
#     prompt += f"{text}\n"

#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=500,
#         n=1,
#         stop=None,
#         temperature=0.0,
#     )

#     reply = response.choices[0].text.strip()

#     return reply


# # st.markdown(message)
# # st.markdown(content)
# while (True):
#     message = input("Enter Your Prompt: ")
#     print(message)
#     bard_anwer = Bard().get_answer(str(message))["content"]
#     chatgpt_answer = generate_answer(message)
#     st.header(':green[ChatGPT] vs :blue[Google Bard]')

#     st.title('Promt:+ '+message)

#     col1, col2 = st.columns(2)
#     print(chatgpt_answer)

#     with col1:
#         st.header("openAI")
#         #    st.text_area(chatgpt_answer)
#         st.markdown(chatgpt_answer)

#     with col2:
#         st.header("Bard")
#         #    st.text_area(bard_anwer)
#         st.markdown(bard_anwer)


