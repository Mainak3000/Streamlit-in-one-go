import streamlit as st

st.title('Title -> Hello everyone, Welcome to my first app')                 #Title
st.header('Header -> First app')                                             #Header
st.subheader('Subheader -> First app')                                       #Subheader
st.text('''Text -> text paragraph, text paragraph, text paragraph,           
        text paragraph, text paragraph, text paragraph, 
        text paragraph, text paragraph, text paragraph,
        text paragraph, text paragraph, text paragraph,''')                  #Text

st.markdown('# Hi')                                                          #Markdown
st.markdown('## Hi')
st.markdown('### Hi')

st.success('Data submitted successfully')                                    #Success
st.info('Information displayed')                                             #Info
st.warning('Warning!')                                                       #Warning
st.error("Error!")                                                           #Error

exp = ZeroDivisionError('Division not possible with 0')
st.exception(exp)                                                            #Exception

st.subheader('Help')
st.help(ZeroDivisionError)                                                   #Help

st.subheader('Write')
st.write('range(1,10)')                                                      #Write
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

st.subheader('Code')
st.code('x = 10\n'                                                           #Code
        'for i in range(x):\n'
        '\tprint(i)')

st.subheader('checkbox')
st.checkbox('Male')                                                          #Checkbox
st.checkbox('Female')

if(st.checkbox('Adult')):
    st.write("You're an adult!")
elif(st.checkbox('Minor')):
    st.write("You're not an adult!")


st.subheader('Radio button')                                                 #Radio Button
st.radio('Select: ', ('Male', 'Female', 'Other'))

radioButton = st.radio('Select age: ', ('0-6', '6-12', '12-18', '18-24', 'above 24'))
if(radioButton == '0-6' or radioButton == '6-12' or radioButton == '12-18'):
    st.write("You're not an adult")
elif(radioButton == '18-24' or radioButton == 'above 24'):
    st.write("You're an adult")


st.subheader('Select Box')                                                    #Select Box
selectBox =  st.selectbox("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                'Deep Learning','Natural Language Processing',
                                                'Computer Vision','Image Processing'])
st.write("You've selected", selectBox)

st.subheader("Multiselect box")                                               #Multi Select Box
MultiSelectBox =  st.multiselect("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                       'Deep Learning','Natural Language Processing',
                                                       'Computer Vision','Image Processing'])
st.write("You've selected : ", len(MultiSelectBox), MultiSelectBox)


st.subheader("Button")
if(st.button("Click me")):                                                    #Button
        st.write("Thanks for clicking me")


st.subheader("Slider")                                                        # Slider
level = st.slider('Select level : ', 1, 100, step=1)
st.write("Level -"+str(level))

st.subheader("Text Input")                                                    # Text-Input
username = st.text_input("Username : ")
password = st.text_input("Password : ", type = "password")
if (username) and (password):
       st.write("Hi, ",username)


st.subheader("Text Area")                                                     # Text-Area
st.text_area("Write something about yourself in 500 words: ")

st.subheader("Input Number")                                                  # Input-Number
st.number_input("Select age :", 18, 90, step=2)

st.subheader("Input Date")                                                    # Input-Date
st.date_input("Date")

st.subheader("Input Time")                                                    # Input-Time
st.time_input("Time")
