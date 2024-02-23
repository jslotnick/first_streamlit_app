import streamlit
import pandas
import requests
import snowflake.connector
import urllib.error 
#import URLError

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("My Mom's new Healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
   
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
# adding some default selections to the selector

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#only show the selected fruits
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruitvice_normalized

#############################
#New Section to display fruitvice api response

streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
   if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
   else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
      
except URLError as e:
   streamlit.error()

#streamlit.write('The user entered ', fruit_choice)

#streamlit.text(fruityvice_response.json())
#Puts it isnto a panda data frame
# my guess is it give it puts names

#################################


streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
#streamlit.text("The fruit load list contains:")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)

add_my_fruit = streamlit.text_input('What more fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding  ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
