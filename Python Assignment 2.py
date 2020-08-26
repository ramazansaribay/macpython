print("Please press any button for yes and press just enter for no")
age = input("Are you a cigarette addict older than 75 years old?")
chronic = input("Do you have a severe chronic disease?")
immune = input("Is your immune system too weak?")
h_risk = "You have a high risk to catch Covid-19."
l_risk = "You are not in the risk group, but you should be careful anyway."
m_risk = "You have a medium risk to catch Covid. Be careful"
if age and chronic and immune:
    print(h_risk)
elif age or chronic or immune:
    print(m_risk)
else:
    print(l_risk)

