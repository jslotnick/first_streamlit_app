import streamlit
#import requests
#import snowflake.connector
#import urllib.error 
#import URLError
streamlit.title("My Mom's new Healthy Diner")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit'
                                       )
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)


# adding some default selections to the selector


#only show the selected fruits


#try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#      streamlit.error("Please select a fruit to get information.")
#   else:
#      back_from_function = get_fruityvice_data(fruit_choice)
#      streamlit.dataframe(back_from_function)
      
# except URLError as e:
