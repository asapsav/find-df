import streamlit as st
import json
import dotenv
import os
import requests
dotenv.load_dotenv()
import openai
import networkx as nx
import matplotlib.pyplot as plt


YOUDOTCOM_API_KEY = os.getenv("YOUDOTCOM_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
OPENAI_MODEL = "gpt-4-1106-preview"

def get_ai_snippets_for_query(query):
    headers = {"X-API-Key": YOUDOTCOM_API_KEY}
    params = {"query": query}
    return requests.get(
        f"https://api.ydc-index.io/search?query={query}",
        params=params,
        headers=headers,
    ).json()


def get_openai_completions(prompt):
    messages = [
        {"role": "system", "content": "You are a helpfull assistant that is an exper biologist and chemo informatitian"}
    ]
    messages.append({"role": "user", "content": prompt})
    
    completion = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=messages
    )
    
    assistant_message = completion.choices[0].message['content']
    messages.append({"role": "assistant", "content": assistant_message})

    return assistant_message





# Main application
def main():
    st.title("Get RAG on your molecule")
    st.markdown("""* BARTsmiles Paper: https://arxiv.org/pdf/2211.16349.pdf
                * S3 Bucket with molecules: https://registry.opendata.aws/usearch-molecules/
                """)

    # Input section
    smiles = st.text_input("Enter Molecule SMILES")
    
    if st.button("Get info"):
        if smiles:
            output = get_ai_snippets_for_query(f"small molecule :{smiles} and cancer")
            st.success("finished YOU.COM Search, getting GPT-4 summary")
            summary = get_openai_completions(f"Sumamrise this:{output}")
            st.subheader("YOU.COM Search Summary")
            st.markdown(f"{summary}")

            st.subheader("VDB Search Results")

            st.subheader("Smth else")

        else:
            st.error("Please inout serach query.")

if __name__ == "__main__":
    main()
