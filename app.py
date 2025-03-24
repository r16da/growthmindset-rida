import streamlit as st

st.set_page_config(page_title="Growth Mindset", page_icon=":smiley:", layout="wide")

st.title("Growth Mindset")

st.write("This is a simple app to help you practice a growth mindset.")

st.header("🚀Welcome to your Growth Mindset Journey")
st.write("This app is designed to help you develop a growth mindset, which is a belief that your abilities and intelligence can be developed through dedication and effort.")

st.header("💡What is a Growth Mindset?")
st.write("A growth mindset is a belief that your abilities and intelligence can be developed through dedication and effort.")

st.header("🎯 What's your challenge today?")
user_input= st.text_input("Enter your challenge here")
if user_input:
    st.successfully(f"Successfully saved your challenge: {user_input}")
else:
    st.warning("Please enter a challenge")

st.header(" 🧠 Reflect on your challange")
reflection=st.text_area("Write about your challenge here")
if reflection:
    st.success("Successfully saved your reflection")
else:
    st.warning("Please write about your challenge")

st.header("🎉 Congratulations on your achievements")
achievements=st.text_area("Write about your achievements here")
if achievements:
    st.success("Successfully saved your achievements")
else:
    st.info("Big or small, every achievement is a step towards your goals")

st.write("Thank you for using the Growth Mindset app! Keep up the good work and remember to celebrate every achievement.")

st.write("---")
st.write("Made with ❤️ by [Rida](https://github.com/r16da)")    


cicpUv-0fixcu-kakcun



