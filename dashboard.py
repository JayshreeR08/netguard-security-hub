import streamlit as st
import pandas as pd
import plotly.express as px
import time  # <-- Added for the real-time clock countdown
from sklearn.ensemble import IsolationForest

# Page configuration
st.set_page_config(page_title="NetGuard Security Hub", layout="wide", initial_sidebar_state="expanded")

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    .stMetric { background-color: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #38bdf8; box-shadow: 0px 4px 10px rgba(56, 189, 248, 0.2); }
    .beginner-box { background: linear-gradient(135deg, #1e1b4b, #311042); padding: 25px; border-radius: 20px; border-left: 8px solid #a855f7; margin-bottom: 25px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3); }
    .animal-card { background-color: #1e293b; padding: 15px; border-radius: 12px; border: 1px solid #475569; text-align: center; margin-bottom: 15px; }
    .footer { text-align: center; padding: 30px; font-size: 20px; font-weight: bold; background: linear-gradient(90deg, #ec4899, #8b5cf6, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; border-top: 1px solid #334155; margin-top: 50px; }
    </style>
""", unsafe_allow_html=True)

# --- 🐾 LEFT SIDEBAR ANIMAL COMPANION ZOO ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #00ffcc;'>🐾NetGuard Buddies</h2>", unsafe_allow_html=True)
    st.write("Your active backend crew keeping the servers cozy:")
    
    st.markdown("""
        <div class="animal-card">
            <h1 style='margin:0; font-size: 50px;'>🐱</h1>
            <b style='color: #38bdf8;'>Node Operator Kitty</b>
            <p style='font-size: 13px; color: #94a3b8; margin: 5px 0 0 0;'>Status: Tracking live data streams...</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="animal-card">
            <h1 style='margin:0; font-size: 50px;'>🤖</h1>
            <b style='color: #a855f7;'>Shield Bot</b>
            <p style='font-size: 13px; color: #94a3b8; margin: 5px 0 0 0;'>Status: Firewall loops active...</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⚙️ Engine State")
    # Dynamically toggles to show users that the feed is live!
    st.success("⚡ LIVE STREAMING MODE ACTIVE")

# --- MAIN HEADER SECTION ---
st.title("🏁 NetGuard Security Hub")
st.markdown("### *Next-Gen Machine Learning System Monitor*")

# --- 💡 BEGINNER-FRIENDLY KNOWLEDGE CORNER ---
st.markdown("""
    <div class="beginner-box">
        <h3 style='color: #c084fc; margin-top: 0;'>💡 New to NetGuard? Here are the 3 ways to read the graphs!</h3>
        <p style='font-size: 16px; line-height: 1.6;'>
            We have built <b>three different visual maps</b> so anyone can understand this computer's health at a glance:
        </p>
        <ol style='font-size: 15px; line-height: 1.7;'>
            <li><b>The Behavioral Cluster Map (Scatter Plot):</b> Shows how the AI groups data. Isolated dots flying away from the main groups turn hot pink—meaning the AI caught an anomaly!</li>
            <li><b>The System Timeline (Line Graph):</b> Shows your computer usage over time. Watch how the lines spike up and down like a live heartbeat monitor.</li>
            <li><b>The Threat Status Share (Pie Chart):</b> A simple breakdown showing the total percentage of safe operations versus detected anomalies.</li>
        </ol>
        <span style='background-color: #00ffcc; color: black; padding: 4px 10px; border-radius: 5px; font-weight: bold; font-size: 13px;'>🟢 Cyan = Safe Baseline</span>
        <span style='background-color: #ff0055; color: white; padding: 4px 10px; border-radius: 5px; font-weight: bold; font-size: 13px; margin-left: 10px;'>🔴 Hot Pink = AI Alerts</span>
    </div>
""", unsafe_allow_html=True)

# --- LIVE DATA LOOP ---
try:
    df = pd.read_csv("system_logs.csv")
    X = df[["CPU_Usage", "Memory_Usage"]]
    
    model = IsolationForest(contamination=0.15, random_state=42)
    df['Anomaly_Score'] = model.fit_predict(X)
    df['Status'] = df['Anomaly_Score'].map({1: 'Safe Baseline (Normal)', -1: 'AI Alert (Anomaly)'})

    # --- GLOWING METRICS ROW ---
    latest = df.iloc[-1]
    m_col1, m_col2, m_col3 = st.columns(3)
    m_col1.metric("💻 Current CPU Load", f"{latest['CPU_Usage']}%")
    m_col2.metric("🧠 Current RAM Allocated", f"{latest['Memory_Usage']}%")
    m_col3.metric("📊 Total Heartbeats Scanned", f"{len(df)} units")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- ROW 1: SCATTER PLOT & PIE CHART ---
    row1_col1, row1_col2 = st.columns([2, 1])

    with row1_col1:
        st.subheader("🎨 1. Behavioral Cluster Map")
        fig = px.scatter(
            df, 
            x="CPU_Usage", 
            y="Memory_Usage", 
            color="Status",
            color_discrete_map={'Safe Baseline (Normal)': '#00ffcc', 'AI Alert (Anomaly)': '#ff0055'},
            hover_data=["Timestamp"],
            template="plotly_dark"
        )
        fig.update_traces(marker=dict(size=11, opacity=0.8))
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)

    with row1_col2:
        st.subheader("📊 2. Threat Status Share")
        pie_fig = px.pie(
            df, 
            names='Status', 
            color='Status',
            color_discrete_map={'Safe Baseline (Normal)': '#00ffcc', 'AI Alert (Anomaly)': '#ff0055'},
            template="plotly_dark"
        )
        pie_fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), showlegend=True, paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(pie_fig, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- ROW 2: LINE GRAPH & GUARD DOG ---
    row2_col1, row2_col2 = st.columns([2, 1])

    with row2_col1:
        st.subheader("📈 3. System Health Timeline")
        line_df = df.melt(id_vars=["Timestamp"], value_vars=["CPU_Usage", "Memory_Usage"], 
                          var_name="Resource", value_name="Percentage")
        
        line_fig = px.line(
            line_df,
            x="Timestamp",
            y="Percentage",
            color="Resource",
            color_discrete_map={'CPU_Usage': '#38bdf8', 'Memory_Usage': '#a855f7'},
            template="plotly_dark"
        )
        line_fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(line_fig, use_container_width=True)

    with row2_col2:
        st.subheader("🦖 Guard Companion")
        st.write("Your system watchdog puppy is sitting tight and happy!")
        
        st.markdown("""
            <div style='background-color: #1e293b; padding: 25px; border-radius: 15px; text-align: center; border: 2px dashed #00ffcc;'>
                <h1 style='font-size: 70px; margin: 0;'>🦖</h1>
                <h3 style='color: #00ffcc; margin: 10px 0 5px 0;'>Net-Dino Guard</h3>
                <p style='font-size: 14px; color: #94a3b8;'>Holding down port 5000 securely!</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("Server Sync Frequency:")
        st.progress(100)

    # --- 🔄 THE REAL-TIME MAGIC TRICK ---
    # Pause for 2 seconds, then tell Streamlit to run this entire file again to load fresh data!
    time.sleep(2)
    st.rerun()

except FileNotFoundError:
    st.error("Missing system_logs.csv! Run live_monitor.py first.")

# --- 👑 SIGNATURE FOOTER ---
st.markdown("""
    <div class="footer">
        🚀 Built by Jayshree Rathore | Empowering Systems with Machine Learning👾
    </div>
""", unsafe_allow_html=True)