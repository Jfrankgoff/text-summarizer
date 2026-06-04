import streamlit as st
from utils.claude_client import summarize_text

st.title("Text Summarizer")
st.write("Powered by Llama (via Ollama)")

text_input = st.text_area("Enter text to summarize", height=200)

input_word_count = len(text_input.split()) if text_input.strip() else 0
st.caption(f"Input word count: {input_word_count}")

length_option = st.select_slider(
    "Summary length",
    options=["Short", "Medium", "Detailed"],
    value="Medium"
)

if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text to summarize.")
    else:
        try:
            with st.spinner("Summarizing..."):
                summary = summarize_text(text_input, length_option)
            st.subheader("Summary")
            st.write(summary)
            output_word_count = len(summary.split())
            st.caption(f"Output word count: {output_word_count}")
        except Exception as e:
            if "model" in str(e).lower() and "not found" in str(e).lower():
                st.error(
                    "Model not found. Pull it by running this in your terminal:\n\n"
                    "```\nollama pull llama3.2\n```"
                )
            else:
                st.error(f"An error occurred: {e}")
