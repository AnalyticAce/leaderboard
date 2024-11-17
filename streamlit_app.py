import streamlit as st
import pandas as pd
from datetime import datetime

final_submission_date = datetime(2024, 11, 30, 23, 42, 00)

current_time = datetime.now()
time_remaining = final_submission_date - current_time

def format_time_delta(delta):
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days} jours, {hours} heures, {minutes} minutes, {seconds} secondes"

data = pd.read_csv('leaderboard.csv')

sorted_data = data.sort_values(by='points', ascending=False)

def assign_medals(index):
    if index == 0:
        return "🥇"
    elif index == 1:
        return "🥈"
    elif index == 2:
        return "🥉"
    else:
        return ""

sorted_data['Medal'] = sorted_data.index.map(assign_medals)

sorted_data['Ranked Name'] = sorted_data['name'] + " " + sorted_data['Medal']

st.set_page_config(page_title="Mois du Numérique", page_icon="🏆", layout="wide")

st.title("🏆 Chasse au Trésor")

st.markdown("""
    <style>
    .card {
        background-color: #ffffff;  /* White background */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;  /* Spacing between cards */
        font-size: 18px;
    }
    .card-header {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
        color: black;  /* Black text */
    }
    .card-body {
        font-size: 20px;
        color: black;  /* Black text */
    }
    h3 {
        text-align: center;  /* Center the h3 header */
        font-size: 28px;
        color: white;  /* White text for header */
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(f"<h3>Temps restant: {format_time_delta(time_remaining)}</h3>", unsafe_allow_html=True)

st.markdown("<h3>Leaderboard</h3>", unsafe_allow_html=True)

for idx, player in sorted_data.iterrows():
    medal = player['Medal']
    name = player['Ranked Name']
    points = player['points']

    st.markdown(f"""
    <div class="card">
        <div class="card-header">{name}</div>
        <div class="card-body">Points: {points}</div>
    </div>
    """, unsafe_allow_html=True)
