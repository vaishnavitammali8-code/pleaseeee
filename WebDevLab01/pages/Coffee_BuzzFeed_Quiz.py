import streamlit as st

st.title("BuzzFeed Quiz")
st.write("Take this quiz to find out what type of coffee lover you are!")

coffee_type = st.radio("What's your go to coffee drink?",
                       ["Espresso", "Latte", "Cappuccino", "Black Coffee"]
                       ) #NEW
coffee_flavors = st.multiselect("What flavors do you like in your coffee?",
                                ["Vanilla","Caramel","Mocha","Hazelnut"]
                                ) #NEW
cups_day = st.number_input("How many cups of coffee do you drink daily?",
                           min_value=0, max_value=10, step=1
                           ) #NEW
coffee_strength = st.slider("How strong do you like your coffee?",
                            1,10,5)

fav_season = st.radio("What's your favorite season?",
                      ["Spring 🌸", "Summer ☀️", "Fall 🍂", "Winter ❄️"]
                      )
st.image("Images/blackcoffee.jpeg")
st.image("Images/pumpkinlattee.jpg")
st.image("Images/flavoredcoffee.jpg")
st.image("Images/milkycoffee.jpg")

if st.button("See your coffee personality!"): #NEW
    st.write("Calculating your coffee personality...")
    st.progress(100) #NEW
    st.balloons() #NEW

if cups_day >= 4 and coffee_type == "Espresso":
    st.write("You are a Coffee Addict! Lots of caffeine!")
elif fav_season == "Fall 🍂":
    st.write("You are a cozy fall coffee lover! We love our Pumpkin Spice!")
elif coffee_type == "Latte":
    st.write("You are a sweet coffee lover! Smooth and sweet.")
elif coffee_flavors:
    st.write("You are the Flavor Master! You love trying out all the new flavors!")
else:
    st.write("You enjoy moderate coffee. Once in a while its nice to have some!")
    


                
