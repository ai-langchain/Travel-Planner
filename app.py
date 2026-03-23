import streamlit as st
from planner import get_destination_info
from optimizer import create_itinerary

st.set_page_config(page_title="Travel Planner System 🌍", layout="centered")

# Custom CSS for better styling
st.markdown("""
<style>
    .cost-positive {
        color: green;
        font-weight: bold;
    }
    .cost-warning {
        color: orange;
        font-weight: bold;
    }
    .cost-negative {
        color: red;
        font-weight: bold;
    }
    .budget-summary {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("✈️ Travel Planner System")
st.markdown("Plan your dream vacation with real cost estimation!")

# Sidebar for budget tips
with st.sidebar:
    st.header("💰 Budget Tips")
    st.info("""
    **Cost Breakdown:**
    - 🎫 Attractions: 70% of budget
    - 🏨 Accommodation: 20%
    - 🍽️ Food: 10%
    
    *Costs shown are estimated attraction entry fees only*
    """)
    
    st.markdown("---")
    st.markdown("**Average Attraction Costs:**")
    st.markdown("- 🏛️ Museums: ₹1500-3000")
    st.markdown("- 🗼 Monuments: ₹1000-2500")
    st.markdown("- 🏞️ Parks: Free-₹500")
    st.markdown("- 🎡 Tourist Spots: ₹2000-4000")

# Main input area
col1, col2 = st.columns(2)
with col1:
    destination = st.text_input("📍 Enter your destination", placeholder="e.g., Paris, Tokyo, New York")
with col2:
    budget = st.number_input("💰 Enter your budget (INR)", min_value=1000, value=50000, step=5000)

# Currency selector
currency = st.selectbox("💱 Currency", ["INR", "USD", "EUR"], index=0)

# Convert currency for display (optional)
if currency != "INR":
    conversion_rate = {"USD": 83, "EUR": 90}.get(currency, 1)
    display_budget = budget / conversion_rate
    currency_symbol = {"USD": "$", "EUR": "€", "INR": "₹"}.get(currency, "₹")
else:
    display_budget = budget
    currency_symbol = "₹"

if st.button("🎯 Generate Smart Plan", type="primary"):
    if not destination:
        st.error("❌ Please enter a destination!")
    else:
        with st.spinner("🌐 Searching for attractions and calculating costs..."):
            # Get attractions
            places = get_destination_info(destination)
            
            if not places:
                st.error("❌ No attractions found for this destination!")
            else:
                # Generate itinerary with cost estimation
                itinerary = create_itinerary(places, budget)
                
                # Calculate total cost
                total_cost = sum(day["cost"] for day in itinerary)
                remaining_budget = budget - total_cost
                accommodation_food_budget = budget * 0.3
                
                # Display Budget Summary
                st.markdown("---")
                st.subheader("💰 Budget Summary")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Budget", f"{currency_symbol}{display_budget:,.0f}")
                with col2:
                    st.metric("Attractions Cost", f"{currency_symbol}{total_cost:,.0f}")
                with col3:
                    if remaining_budget >= 0:
                        st.metric("Remaining Budget", f"{currency_symbol}{remaining_budget:,.0f}", delta="Available")
                    else:
                        st.metric("Budget Status", "Over Budget", delta=f"{currency_symbol}{abs(remaining_budget):,.0f}", delta_color="inverse")
                
                st.info(f"🏨 **Note:** {currency_symbol}{accommodation_food_budget:,.0f} reserved for accommodation & food (30% of total budget)")
                
                # Show attractions
                st.markdown("---")
                st.subheader("📍 Top Attractions Found")
                
                # Create columns for attractions
                cols = st.columns(2)
                for idx, p in enumerate(places[:5], 1):
                    with cols[idx % 2]:
                        st.markdown(f"**{idx}. {p['name']}**")
                        st.markdown(f"[🔗 Learn more]({p['link']})")
                
                # Itinerary with cost breakdown
                st.markdown("---")
                st.subheader("🗓 Smart Itinerary with Cost Breakdown")
                
                # Display itinerary in a table-like format
                for day in itinerary:
                    with st.container():
                        col1, col2, col3 = st.columns([1, 3, 1])
                        with col1:
                            st.markdown(f"**Day {day['day']}**")
                        with col2:
                            st.markdown(f"**{day['place']}**")
                        with col3:
                            if day['cost'] == 0:
                                st.markdown(f"<span class='cost-positive'>💰 Free!</span>", unsafe_allow_html=True)
                            elif day['is_over_budget']:
                                st.markdown(f"<span class='cost-negative'>⚠️ {currency_symbol}{day['cost']:,}</span>", unsafe_allow_html=True)
                            else:
                                st.markdown(f"<span class='cost-warning'>💵 {currency_symbol}{day['cost']:,}</span>", unsafe_allow_html=True)
                        
                        # Add progress bar for daily budget allocation
                        if day['daily_allocation'] > 0:
                            usage_percentage = (day['cost'] / day['daily_allocation']) * 100
                            st.progress(min(usage_percentage / 100, 1.0))
                            st.caption(f"Daily budget allocated: {currency_symbol}{day['daily_allocation']:,.0f} | Used: {usage_percentage:.0f}%")
                        st.markdown("---")
                
                # Budget Recommendations
                st.markdown("---")
                st.subheader("💡 Budget Recommendations")
                
                if remaining_budget > 0:
                    st.success(f"✅ Great! You have {currency_symbol}{remaining_budget:,.0f} remaining. Consider:")
                    st.markdown("""
                    - 🍽️ Try local restaurants
                    - 🛍️ Buy souvenirs
                    - 🚕 Use premium transportation
                    - 🎭 Book additional experiences
                    """)
                elif remaining_budget < 0:
                    st.warning(f"⚠️ You're over budget by {currency_symbol}{abs(remaining_budget):,.0f}. Suggestions:")
                    st.markdown("""
                    - 🎟️ Look for discount passes or combo tickets
                    - 🚶 Choose free attractions
                    - 🍱 Eat at local markets instead of restaurants
                    - 🏨 Consider budget accommodations
                    """)
                else:
                    st.info("🎯 Perfect! Your budget matches the estimated costs exactly!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <small>✨ Pro Tip: Costs are estimates based on average entry fees. Actual prices may vary by season and special events.</small>
</div>
""", unsafe_allow_html=True)
