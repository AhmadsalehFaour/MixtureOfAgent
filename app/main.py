import streamlit as st
from models import load_models
from logic import generate_answers
from utils import init_logger, save_prompt


st.set_page_config(page_title="MoA: Mixture of Agents", layout="centered")
st.title("🧠 Mixture of Agents (MoA)")
st.write("Enter a question, and multiple AI agents will answer and aggregate the responses.")
logger = init_logger()

# 🔘 Mode Selection (Local or Remote)
# 🔘 Choose Local or Remote
model_mode = st.radio(
    "Choose model mode:",
    options=["remote", "local"],
    index=0,
    format_func=lambda x: "Remote (online)" if x=="remote" else "Local (offline)"
)
# Load models + names
proposer1, proposer2, aggregator, model_names = load_models(mode=model_mode)

# UI form
with st.form(key="qa_form"):
    user_input = st.text_area("💬 Your question:", height=150)
    submitted = st.form_submit_button("Generate Answer")

if submitted and user_input.strip():
    logger.info("User prompt: %s", user_input)
    save_prompt(user_input)

    r1, r2, final = generate_answers(user_input, proposer1, proposer2, aggregator, logger)

    st.subheader(f"📌 Proposer 1 ({model_names['p1']})")
    st.write(r1)

    st.subheader(f"📌 Proposer 2 ({model_names['p2']})")
    st.write(r2)

    st.subheader(f"✅ Final Aggregated Response ({model_names['agg']})")
    st.success(final)