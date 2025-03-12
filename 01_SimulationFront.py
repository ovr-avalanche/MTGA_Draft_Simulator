import streamlit as st 
import Simulation

st.set_page_config(
    page_title="MTG_Arena Draft Simulator",  
    page_icon="icon.webp",  
    layout="wide" 
)

st.title("Draft Simulation")

selection = st.sidebar.pills("", ["Quickdraft", "Premierdraft", "Traditional"], selection_mode="single", default="Quickdraft")
if selection == "Quickdraft":
    DraftObject = Simulation.Quickdraft()
else:
    DraftObject = Simulation.Premierdraft()

winrate = st.sidebar.number_input("Winrate", value=0.55, min_value=0.0, max_value=1.0)
number_of_drafts = st.sidebar.number_input("Number of Drafts", value=1, min_value=1, max_value=9000)
starting_diamonds = st.sidebar.number_input("Starting Diamonds", value=10000, min_value=0, max_value=1000000)
Simulation.Diamonds = starting_diamonds




#------------------- Simulion start --------------------

buttonval = st.button("Start Simulation")
diamondlist = [Simulation.Diamonds]
drafts_played = number_of_drafts
if buttonval:
    for x in range(number_of_drafts):
        draft_bool = Simulation.draft_simulation(DraftObject, winrate)
        diamondlist.append(Simulation.Diamonds)
        
        if not draft_bool:
            drafts_played = x
            break

    st.write("Drafts played: ", drafts_played)
    st.write("Diamonds after the simulation: ", Simulation.Diamonds)
    st.line_chart(diamondlist)
    





