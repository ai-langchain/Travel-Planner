# Travel-Planner
🎯 Travel Planner System

An AI-powered application that plans trips for any destination based on top attractions, budget, and personalized itinerary suggestions.

🔍 Turn destinations into insights
🎯 Turn travel plans into day-wise itineraries

📌 Overview

This project fetches real-world top attractions using SerpApi and provides a simple, engaging travel plan.

It allows users to:

Discover must-visit places in any city
Generate a day-wise itinerary
Access links for more information about each attraction

Designed for travelers, students, and anyone looking to plan trips efficiently.

🎯 Objective

This project helps users:

Explore AI-assisted travel planning
Understand multi-agent workflows (Planner + Optimizer)
Learn API integration with Python
Build real-world applications with Streamlit + SerpApi
🚀 Features
🔍 Real-time top attractions search (via SerpApi)
📄 Clickable links to attractions for more details
🗓 Day-wise itinerary generator
💼 Simple, interactive Streamlit interface
🧠 Multi-agent workflow:
Planner: Fetches top attractions
Optimizer: Creates a day-wise itinerary
🧠 Architecture / Workflow
🔄 System Flow

User Inputs:

Destination (e.g., Paris, Tokyo)
Budget (optional)

System Workflow:

Fetches top attractions using SerpApi
Planner Agent: Extracts attraction names & links
Optimizer Agent: Generates a simple day-wise itinerary

Output:

Recommended attractions
Clickable links for more info
Suggested day-wise itinerary
🛠 Tech Stack
Language: Python
UI: Streamlit
API: SerpApi
LLM (Optional for enhancements): Groq / LLaMA 3
Libraries: streamlit, requests, python-dotenv
📁 Project Structure
travel-planner-ai/
│
├── app.py            # Streamlit interface
├── planner.py        # Planner agent (fetch attractions)
├── optimizer.py      # Optimizer agent (create itinerary)
├── requirements.txt
├── .env              # (API key, not uploaded to GitHub)
└── README.md         # Project documentation
⚙️ Setup Instructions
🔧 Prerequisites
Python 3.8+
Git installed
SerpApi key
📦 Installation (Step-by-Step)

1️⃣ Clone the Repository

git clone <your-repo-url>
cd travel-planner-ai

2️⃣ Create Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Setup Environment Variables

Create a .env file:

SERPAPI_API_KEY=your_serpapi_key
▶️ Running the Project
streamlit run app.py

Then open 👉 http://localhost:8501

💻 How It Works (Code-Level)
🔹 get_destination_info()
Fetches top attractions using SerpApi
🔹 plan_trip()
Main Planner agent: extracts attraction names & links
🔹 create_itinerary()
Optimizer agent: creates day-wise itinerary
🔹 app.py
Handles UI: user input → planner → optimizer → display results
🧪 Example Usage

Input:

Destination: Paris
Budget: 5000 INR

Output:

📍 Top Attractions: Eiffel Tower, Louvre Museum, Notre-Dame Cathedral …
🗓 Suggested Itinerary:
Day 1: Eiffel Tower
Day 2: Louvre Museum
Day 3: Notre-Dame Cathedral
🔧 Customization / Extensions
Add budget-based attraction filtering
Add maps visualization
Include hotels / restaurants recommendations
Enhance itinerary optimization based on distance/time
🚀 Future Improvements
Add flight & hotel integration APIs
Deploy online (Streamlit Cloud)
Multi-city trip planning
Personalized travel recommendations using AI
👨‍💻 Contributors
Sherlin A
💡 Quick Notes
Create .env file and add your SerpApi key
Use virtual environment (recommended)
Run streamlit run app.py to launch the app
