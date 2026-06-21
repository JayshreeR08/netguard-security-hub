# NetGuard Security Hub Version 1: AI-Powered System Anomaly Detector

### 🌐 Live Production Dashboard: [Launch NetGuard Live Dashboard](https://jayshreer08-netguard-security-hub-dashboard-gnex5o.streamlit.app/)

NetGuard Security Hub is an end-to-end cybersecurity and system health monitoring ecosystem. The project features a low-level network communication backend, a continuous background data logging pipeline, and an unsupervised Machine Learning engine that detects stealthy system vulnerabilities and behavioral anomalies in real-time.

---

## 🚀 Key Features
- **Unsupervised Anomaly Detection:** Utilizes an Isolation Forest machine learning model to detect complex, multi-variable system deviations that traditional, rigid rule-based systems miss.
- **Multi-Threaded Network Backend:** Features a custom multi-threaded Java TCP Server architecture built for low-latency client-server socket tracking.
- **Relational Data Persistence:** Integrates a structured SQLite database layer ensuring persistent storage, tracking, and auditing of historical system heartbeats.
- **Interactive Cyber-Hub UI:** A highly intuitive, dark-mode analytic interface visualizing resource allocations, real-time alert thresholds, and multi-dimensional cluster distributions.

---

## 🛠️ The Architecture & Tech Stack

This project maps out a full-stack data engineering pipeline across three core layers:
[ Local Client/Server Agent ] ──> [ SQLite Database / CSV ] ──> [ Cloud Streamlit Dashboard ]
(Java TCP Server +               (Structured Storage &         (Scikit-Learn ML Engine &
Python Monitor Engine)             Data Snapshot Layer)            Interactive Visuals)
### Backend & Network Layer
- **Java (JDK):** Low-level socket programming (`GuardServer.java`) implementing server-side port binding and multi-threaded connection handling.
- **Python (3.x):** Background monitoring engine tracking real-time device hardware metrics.

### Storage & Data Engineering
- **SQLite3 / SQL:** Local relational database engine tracking relational transaction history (`netguard.db`).
- **Pandas:** Used for efficient data parsing, structure alignment, and CSV time-series dataset logging.

### Machine Learning & Frontend Visualization
- **Scikit-Learn:** Drives the core `IsolationForest` unsupervised model, mapping structural anomalies by calculating the spatial isolation distances of multi-variable metrics.
- **Streamlit Cloud:** Hosts the production-grade deployment web engine.
- **Plotly Express:** Generates responsive, high-contrast behavioral cluster scatter plots and time-series line graphs.

---

## 🧠 The AI Engine: Why Isolation Forest?
Traditional security systems check for single thresholds (e.g., `if CPU > 90% then ALERT`). However, modern security exploits often utilize stealth tactics that consume minimal resources to avoid detection.

NetGuard implements an **Isolation Forest** model to analyze multi-variable coordinates (CPU vs. RAM balance). For example, if the system logs a **9% CPU usage** alongside an **88% RAM allocation**, the Isolation Forest isolates this rare data point from the normal dense cluster, flagging it instantly as an behavioral anomaly.

---

## 📂 Project Structure & Files
- `dashboard.py`: The production frontend script containing the visual UI layouts, graph plotters, and cloud ML execution.
- `system_logs.csv`: A production-ready snapshot dataset of recorded historical system baseline tracking.
- `requirements.txt`: The environment configuration blueprint managing cloud-hosted libraries and version locking.
- `GuardServer.java` *(Local Deployment)*: Multi-threaded Java socket listener running on host machine.
- `live_monitor.py` *(Local Deployment)*: Background diagnostic crawler tracking host resource telemetry.
- `netguard.db` *(Local Deployment)*: Relational SQL database mapping persistent system histories.

---
*Developed as an engineering portfolio piece demonstrating end-to-end full-stack development, network socket administration, and applied unsupervised machine learning.*


---
##Author
Jayshree
