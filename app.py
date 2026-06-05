import streamlit as st
from utils.claude_client import summarize_text, DEFAULT_MODEL

st.title("Text Summarizer")
st.write("Powered by Claude (Anthropic)")

text_input = st.text_area("Enter text to summarize", height=200)

input_word_count = len(text_input.split()) if text_input.strip() else 0
st.caption(f"Input word count: {input_word_count}")

length_option = st.select_slider(
    "Summary length",
    options=["Short", "Medium", "Detailed"],
    value="Medium"
)

model_option = st.sidebar.selectbox(
    "Model",
    options=["claude-haiku-4-5", "claude-sonnet-4-6", "claude-opus-4-8"],
    index=0,
)

if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text to summarize.")
    else:
        try:
            with st.spinner("Summarizing..."):
                summary = summarize_text(text_input, length_option, model=model_option)
            st.subheader("Summary")
            st.write(summary)
            output_word_count = len(summary.split())
            st.caption(f"Output word count: {output_word_count}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
