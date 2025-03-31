import streamlit as st

st.set_page_config(page_title="Muhammad Ahsan Alvi Growth Mindset Project", page_icon="🌟")
st.title("Muhammad Ahsan Alvi Growth Mindset AI Project")

st.header("💞 Welcome to Your Growth Journey")
st.write(
    "This AI-powered app helps you build a growth mindset by providing you with the tools and resources you need "
    "to overcome challenges and achieve your goals. Whether you're looking to improve your skills, build new habits, "
    "or develop a positive mindset, this app has everything you need to succeed. Let's get started! 💪🚀"
)

# Quote section
st.header("💚 Today's Growth Mindset Quote")
st.write("“Success is not final, failure is not fatal: It is the courage to continue that counts.” - Winston Churchill")

# User challenge input
st.header("♡ What's Your Challenge Today?")
user_input = st.text_input("Describe your challenge today", "e.g. I'm struggling to stay focused on my work")

if user_input:
    st.success(f"💪 You're facing: {user_input}. Keep pushing forward toward your goal! 💪")
else:
    st.warning("🤔 What's your challenge today?")

# Reflection section
st.header("🌟 Reflect on Your Learning")
reflection = st.text_area(
    "Write your reflection here", 
    "e.g. What did you learn today? What challenges did you face? How can you overcome them?"
)

if reflection:
    st.success(f"🌟 Great Insight! Your reflection: {reflection} 🌟")
else:
    st.info("🤔 Reflecting on past experiences helps you grow! Share your thoughts.")

# Achievements section
st.header("🏆 Celebrate Your Achievements!")
achievement = st.text_input("Share something you've achieved today", "e.g. I completed my project ahead of schedule")

if achievement:
    st.success(f"🎉 Congratulations! You've achieved: {achievement} 🎉")
else:
    st.info("🤔 Big or small, every achievement counts! Share one now! ❤️")

# Footer
st.write("----")
st.write("👭 Keep believing in yourself. Growth is a journey, not a destination. Keep pushing forward and you'll achieve great things! 💖")
st.write("🌟 Created with love by Muhammad Ahsan Alvi🌟")
