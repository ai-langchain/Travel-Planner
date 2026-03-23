# app.py
import streamlit as st
from planner import plan_trip
from optimizer import create_itinerary

st.set_page_config(page_title="Travel Planner System 🌍", layout="centered")
st.title("✈️ Travel Planner System")

destination = st.text_input("Enter your destination (e.g., Paris)")
budget = st.number_input("Enter your budget (INR)", min_value=0)

if st.button("Generate Plan"):
    if not destination:
        st.error("Please enter a destination!")
    else:
        st.info("Planning your trip…")
        plan = plan_trip(destination, budget)

        if plan.get("error"):
            st.error(plan["error"])
        else:
            # Show attractions
            st.subheader("📍 Recommended Places")
            for idx, p in enumerate(plan["places"], 1):
                st.write(f"{idx}. {p['name']} — [Link]({p['link']})")

            # Itinerary
            st.subheader("🗓 Suggested Itinerary")
            itinerary = create_itinerary(plan["places"])
            for i in itinerary:
                st.write(f"Day {i['day']}: {i['place']} — Cost: ₹{i['cost']}")