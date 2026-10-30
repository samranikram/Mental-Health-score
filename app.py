import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="Mental Health Score Predictor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS Styling for a Modern Look
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #4A90E2;
        text-align: center;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #666666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #4A90E2 0%, #50E3C2 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.75rem;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    .stButton>button:hover {
        opacity: 0.9;
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="main-header">🧠 Mental Health Score Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Apni daily habits aur lifestyle details darj karein taake mental health score ka andaza lagaya ja sakay.</div>', unsafe_allow_html=True)

# Layout using Columns & Containers
with st.form("prediction_form"):
    
    st.markdown("### 📋 Personal & Academic Information")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", min_value=10, max_value=100, value=20)
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col3:
        country = st.text_input("Country", value="India")
        
    col4, col5 = st.columns(2)
    with col4:
        academic_level = st.selectbox("Academic Level", ["Undergraduate", "Graduate", "High School"])
    with col5:
        stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High", "Very High"])

    st.markdown("---")
    st.markdown("### 📱 Digital Usage & Habits")
    col6, col7, col8 = st.columns(3)
    
    with col6:
        most_used_platform = st.selectbox("Most Used Platform", [
            "Facebook", "LinkedIn", "Instagram", "Snapchat", "Twitter", 
            "YouTube", "TikTok", "LINE", "KakaoTalk", "VKontakte", "WhatsApp", "WeChat"
        ])
    with col7:
        purpose_of_use = st.selectbox("Purpose of Use", ["Networking", "Education", "Entertainment", "News"])
    with col8:
        daily_unlocks = st.number_input("Daily Phone Unlocks", min_value=0, value=50)

    avg_daily_usage_hours = st.slider("Avg Daily Usage Hours", min_value=6.0, max_value=24.0, value=8.0, step=0.5)

    st.markdown("---")
    st.markdown("### 🛌 Lifestyle & Daily Routine")
    col9, col10, col11 = st.columns(3)
    
    with col9:
        study_hours = st.slider("Study Hours", min_value=0.0, max_value=24.0, value=4.0, step=0.5)
    with col10:
        physical_activity_hours = st.slider("Physical Activity Hours", min_value=0.0, max_value=24.0, value=1.0, step=0.5)
    with col11:
        sleep_hours_per_night = st.slider("Sleep Hours Per Night", min_value=0.0, max_value=24.0, value=7.0, step=0.5)

    st.markdown("")
    # Submit Button inside form
    submitted = st.form_submit_button("Predict Mental Health Score 🚀")

if submitted:
    payload = {
        "age": age,
        "gender": gender,
        "country": country,
        "academic_level": academic_level,
        "most_used_platform": most_used_platform,
        "purpose_of_use": purpose_of_use,
        "avg_daily_usage_hours": avg_daily_usage_hours,
        "daily_unlocks": daily_unlocks,
        "study_hours": study_hours,
        "physical_activity_hours": physical_activity_hours,
        "sleep_hours_per_night": sleep_hours_per_night,
        "stress_level": stress_level
    }
    
    try:
        with st.spinner("Analyzing data through AI model... ⏳"):
           response = requests.post("https://mental-health-score-rvx5.onrender.com/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            score = result.get("predicted_mental_health_score")
            
            st.balloons()
            st.success(f"### 🎉 Predicted Mental Health Score: **{score}**")
        else:
            st.error(f"Server Error: {response.text}")
            
    except Exception as e:
        st.error(f"FastAPI backend se connection nahi ho saka. Make sure uvicorn is running! \nError: {e}")