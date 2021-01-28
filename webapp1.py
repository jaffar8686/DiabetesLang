import streamlit as st
import seaborn as sns
import pandas as pd
from PIL import Image
import pickle
from google_trans_new import google_translator  
translator=google_translator()
st.sidebar.header("Welcome")
st.sidebar.subheader("language option")
a=st.sidebar.checkbox('Hindi')
b=st.sidebar.checkbox('Telugu')
c=st.sidebar.checkbox('Japanese')
d=st.sidebar.checkbox('German')
def lang():
    
    if a:
        
        return 'hi'
    elif b:
        return 'te'
    elif c:
        
        return 'ja'
    elif d:
        return 'de'
    else:
        return 'en'


title='Daibetes Checkup'
t_text = translator.translate(title,lang_tgt=lang())

st.title(t_text)
img = Image.open("diabetes1.jpg")
st.image(img,width=500,caption="diabetes")
title='diabetes is one of the major health issue'
text1=translator.translate(title,lang_tgt=lang())
st.write(text1)
title="""people need to eat less sweets to get rid from
            the dangeorus disease called diabetes"""
text1=translator.translate(title,lang_tgt=lang())
st.markdown(text1)
st.write("Dataset")
df=pd.read_csv("diabetes.csv")
st.write(df.head())
title='enter the pregnancy value'
text1=translator.translate(title,lang_tgt=lang())
p = st.number_input(text1)


title="enter the glucose value"
text1=translator.translate(title,lang_tgt=lang())
g = st.number_input(text1)

title="enter the bloodpressure value"
text1=translator.translate(title,lang_tgt=lang())
bp= st.number_input(text1)

title="enter the Skin thickness value"
text1=translator.translate(title,lang_tgt=lang())
sti= st.number_input(text1)

title="enter the insulin value"
text1=translator.translate(title,lang_tgt=lang())
ins = st.number_input(text1)

title='enter the BMI value'
text1=translator.translate(title,lang_tgt=lang())
bmi= st.number_input(text1)

title="enter the Diabetes pedigree function value"
text1=translator.translate(title,lang_tgt=lang())
dpf = st.number_input(text1)

title='enter the age'
text1=translator.translate(title,lang_tgt=lang())
a= st.number_input(text1)
output=[]
lst=[p,g,bp,sti,ins,bmi,dpf,a]
output.append(lst)
with open("model1","rb")as f:
    model=pickle.load(f)
    
title="Predict"
text11=translator.translate(title,lang_tgt=lang())
button=st.button(text11)
if button:
    outcome=model.predict(output)
    #st.write(outcome)
    st.write()
    if(outcome==1):
        title="Diabetic"
        text1=translator.translate(title,lang_tgt=lang())
        st.write(text1)
    else:
        title="Non Diabetic"
        text1=translator.translate(title,lang_tgt=lang())
        st.write(text1)
title1='correlation'
text12=translator.translate(title1,lang_tgt=lang())
if st.checkbox(text12):
    st.write(sns.heatmap(df.corr()))
    st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)
    

