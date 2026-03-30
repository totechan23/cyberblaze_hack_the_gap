import streamlit as st
import requests
import json
from datetime import datetime

# Page config
st.set_page_config(
    page_title="AI Civic Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    }
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        display: flex;
        gap: 0.5rem;
    }
    .user-message {
        background-color: #00c6ff;
        color: black;
        margin-left: 2rem;
    }
    .ai-message {
        background-color: #2a2a40;
        color: white;
        margin-right: 2rem;
    }
    .sidebar .sidebar-content {
        background: #1a1a2e;
    }
    </style>
""", unsafe_allow_html=True)

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000"

# Initialize session state
if "role" not in st.session_state:
    st.session_state.role = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "complaints" not in st.session_state:
    st.session_state.complaints = []

# Sidebar Navigation
with st.sidebar:
    st.title("🚀 AI Civic Assistant")
    st.markdown("---")
    
    if st.session_state.role:
        st.success(f"Role: **{st.session_state.role.upper()}**")
        
        if st.button("🚪 Logout", key="logout_btn", use_container_width=True):
            st.session_state.role = None
            st.session_state.chat_history = []
            st.session_state.complaints = []
            st.rerun()
    else:
        st.info("👤 Not logged in")
    
    st.markdown("---")
    st.subheader("Select Role")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👨‍💼 Citizen", key="citizen_btn", use_container_width=True):
            st.session_state.role = "citizen"
            st.session_state.chat_history = []
            st.rerun()
    
    with col2:
        if st.button("👨‍💻 Employee", key="employee_btn", use_container_width=True):
            st.session_state.role = "employee"
            st.session_state.chat_history = []
            st.rerun()

# Main Content
if not st.session_state.role:
    st.title("🎯 Welcome to AI Civic Assistant")
    st.markdown("""
    ### Smart Complaint & SOS System
    
    Select your role in the sidebar to get started:
    - **👨‍💼 Citizen**: Report complaints or emergency SOS
    - **👨‍💻 Employee**: Manage and track complaints
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Features", "2", "+1 new")
    with col2:
        st.metric("Quick Response", "AI-Powered", "24/7")
    with col3:
        st.metric("Priority Routing", "Smart", "Active")

elif st.session_state.role == "citizen":
    st.title("💬 Citizen Dashboard - AI Complaint Assistant")
    st.markdown("Report complaints or request emergency help")
    st.markdown("---")
    
    # Chat display
    chat_container = st.container()
    
    with chat_container:
        if len(st.session_state.chat_history) == 0:
            st.info("💡 Try: 'water leakage' or 'I am unsafe'")
        
        for msg in st.session_state.chat_history:
            if msg["sender"] == "You":
                with st.chat_message("user"):
                    st.write(msg["text"])
            else:
                with st.chat_message("assistant"):
                    st.write(msg["text"])
    
    st.markdown("---")
    
    # Input area
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input(
            "Enter complaint or SOS...",
            key="citizen_input",
            label_visibility="collapsed"
        )
    
    with col2:
        send_btn = st.button("📤 Send", key="send_btn", use_container_width=True)
    
    if send_btn and user_input.strip():
        # Add user message to chat
        st.session_state.chat_history.append({"sender": "You", "text": user_input})
        
        # Send to backend
        try:
            response = requests.post(
                f"{BACKEND_URL}/ai/chat",
                json={"message": user_input},
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                ai_reply = data.get("reply", "✅ Complaint registered!")
            else:
                ai_reply = "⚠️ Error processing request"
        except Exception as e:
            ai_reply = f"❌ Connection error: {str(e)}"
        
        # Add AI response to chat
        st.session_state.chat_history.append({"sender": "AI", "text": ai_reply})
        st.rerun()

elif st.session_state.role == "employee":
    st.title("📊 Employee Dashboard")
    st.markdown("View and manage all complaints")
    st.markdown("---")
    
    # Refresh button
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("🔄 Refresh", key="refresh_btn", use_container_width=True):
            st.session_state.complaints = []
    
    # Fetch complaints
    try:
        response = requests.get(f"{BACKEND_URL}/employee/dashboard", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            complaints = data.get("complaints", [])
            st.session_state.complaints = complaints
        else:
            st.error("Failed to fetch complaints")
            complaints = []
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
        complaints = st.session_state.complaints
    
    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Complaints", len(complaints))
    with col2:
        pending = sum(1 for c in complaints if c.get("status", "") == "Pending")
        st.metric("Pending", pending)
    with col3:
        resolved = sum(1 for c in complaints if c.get("status", "") == "Resolved")
        st.metric("Resolved", resolved)
    with col4:
        urgent = sum(1 for c in complaints if "danger" in str(c).lower() or "unsafe" in str(c).lower())
        st.metric("🚨 Urgent", urgent)
    
    st.markdown("---")
    
    # Complaints list
    if len(complaints) == 0:
        st.info("ℹ️ No complaints yet")
    else:
        st.subheader("📋 All Complaints")
        
        for idx, complaint in enumerate(complaints):
            with st.expander(
                f"Complaint #{complaint.get('id', idx+1)} - {complaint.get('status', 'Pending')}",
                expanded=False
            ):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.write(f"**User:** {complaint.get('user', 'Anonymous')}")
                    st.write(f"**Message:** {complaint.get('text', 'N/A')}")
                    st.write(f"**Status:** {complaint.get('status', 'Pending')}")
                    if complaint.get('location'):
                        st.write(f"**Location:** {complaint.get('location')}")
                    if complaint.get('priority'):
                        st.write(f"**Priority:** {complaint.get('priority')}")
                
                with col2:
                    st.write("**Actions**")
                    if st.button("✅ Resolve", key=f"resolve_{idx}"):
                        st.success("Marked as resolved!")
                    if st.button("⚠️ Escalate", key=f"escalate_{idx}"):
                        st.warning("Escalated to senior staff!")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888;'>
    <p>🔐 AI Civic Assistant v1.0 | Smart Complaint & SOS System</p>
    </div>
""", unsafe_allow_html=True)
