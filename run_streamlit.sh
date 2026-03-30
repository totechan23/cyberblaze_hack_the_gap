#!/bin/bash

echo "🚀 Starting CyberBlaze Stack..."
echo ""

# Check if backend is running
echo "📡 Checking backend..."
if ! curl -s http://127.0.0.1:8000/ > /dev/null 2>&1; then
    echo "⚠️  Backend not running. Starting..."
    cd backend
    python -m pip install -q -r requirements.txt
    python app.py &
    BACKEND_PID=$!
    sleep 2
    echo "✅ Backend started (PID: $BACKEND_PID)"
    cd ..
else
    echo "✅ Backend already running"
fi

echo ""
echo "🎨 Starting Streamlit frontend..."
python -m pip install -q -r streamlit_requirements.txt
streamlit run streamlit_app.py
