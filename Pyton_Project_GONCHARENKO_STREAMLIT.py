import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load data
data = pd.read_csv('Apex_Legends_DATA_TABLE.csv')

# Display basic statistics
st.write("### Mean,median and standard deviation of 3 fields")
st.write("Player Damage:", data['my_damage'].describe())
st.write("Teammate 1 Damage:", data['teamate_1_damage'].describe())
st.write("Teammate 2 Damage:", data['teamate_2_damage'].describe())

# Check for missing data
st.write("### Pfoof of data clearence")
if data.isna().any().any():
    st.write("### Missing Data")
    st.write("There is missing data in the dataset.")
else:
    st.write("### Missing Data")
    st.write("No missing data found in the dataset.")

# Define additional arrays for additional analysis

rp_earned = data['rp_earned'].tolist()
team_kills = data['team_kills'].tolist()
place = data['squad_placed'].tolist()
number = data['counter'].tolist()
team_damage = data['team_damage'].tolist()
meta_points = data['meta_score'].tolist()
squad = data['premade_squad'].tolist()

# General plots of dependence of a Ranked Points earned from amount of kills.

st.write("### Dependence of Ranked Points on Amount of Kills")
fig1, ax1 = plt.subplots()
ax1.stem(rp_earned, team_kills)
ax1.set_xlabel('Ranked Points Earned')
ax1.set_ylabel('Number of Kills')
ax1.set_title('Dependence of Ranked Points on Amount of Kills')
st.pyplot(fig1)

#General plot of dependence of kills from damage. 100-200 damage is an average amount of damage you need to deal in order to get a kill. 

st.write("### Dependence of Damage on Kills")
fig2, ax2 = plt.subplots()
ax2.scatter(team_damage, team_kills)
ax2.set_xlabel('Amount of Damage Dealt by Team')
ax2.set_ylabel('Number of Kills Made by Team')
ax2.set_title('Dependence of Number of Kills on Amount of Damage')
st.pyplot(fig2)

#General plot of place in the game

st.write("### Overall Place Statistic")
fig3, ax3 = plt.subplots()
ax3.scatter(place, number)
ax3.set_xlabel('Game Number')
ax3.set_ylabel('Place')
ax3.set_title('Overall Place Statistic')
st.pyplot(fig3)

#Amount of kills commited by team and amount of damage dealt by team influence place in the game.

# Comparative plots 
st.write("### Placement vs Damage and Kills Comparasent")
fig4, ax4 = plt.subplots()
ax4.scatter(place, team_damage)
ax4.set_xlabel('Place')
ax4.set_ylabel('Amount of Damage Dealt by Team')
ax4.set_title('First Comparative Plot: Dependence of Placement on Amount of Damage')
st.pyplot(fig4)



fig5, ax5 = plt.subplots()
ax5.scatter(place, team_kills)
ax5.set_xlabel('Place')
ax5.set_ylabel('Number of Kills Made by Team')
ax5.set_title('Second Comparative Plot: Dependence of Placement on Number of Kills')
st.pyplot(fig5)

#In season 15 of apex legends best legends to play were: Horizon,Seer,Gibraltar,Valkyrie,Wraith,Bloodhound,Newcastle
#To understand this, i have analysed 4 tierlists from season 15
#Worst legends to play were: Mirage, Revenant
#I have made a column on this topic with logic: every legend from the S-tier gives +1 point to 'Meta' count and D-tier gives -1 point

st.write("### Meta Score vs Team Damage and Team Kills")
fig6, ax6 = plt.subplots()
ax6.scatter(meta_points, team_damage)
ax6.set_xlabel('Meta Score')
ax6.set_ylabel('Amount of Damage')
ax6.set_title('First Comparative Plot: Dependence of Meta Score on Damage')
st.pyplot(fig6)



fig7, ax7 = plt.subplots()
ax7.scatter(meta_points, team_kills)
ax7.set_xlabel('Meta Score')
ax7.set_ylabel('Number of Kills')
ax7.set_title('Second Comparative Plot: Dependence of Meta Score on Kills')
st.pyplot(fig7)

#Meta influences almost 0 to none on both kills and placement, best games were played with legends not included in D or S rank.

# Hypothesis about premade team
st.write("### My Hypothesis Is That Preassembled Teams Lead to Higher Ranked Points Earnings")
squad_data_converted = [1 if yn == 'yes' else 0 for yn in squad]
premade_rpt = premade_c = non_premade_rpt = non_premade_c = 0

for i in range(len(rp_earned)):
    if squad_data_converted[i] == 1:
        premade_rpt += rp_earned[i]
        premade_c += 1
    else:
        non_premade_rpt += rp_earned[i]
        non_premade_c += 1

average_premade_rpt = premade_rpt // premade_c if premade_c else 0
average_non_premade_rpt = non_premade_rpt // non_premade_c if non_premade_c else 0

st.write(f"Average Ranked Points Earned (Premade Team): {average_premade_rpt}")
st.write(f"Average Ranked Points Earned (Non-Premade Team): {average_non_premade_rpt}")
st.write("I have counted total ernings from games played with premade team and without, then divided both on amount of games played that same way")
st.write("And therefore got average amount of points earned per game.")
st.write("Here we see proof of my hypothesis. Premade team leads to more then twice as much points earned in one game on average then non-premade team.")
st.write("Also during the process i have made 4 additional columns made from operations with 3 different columns on average")