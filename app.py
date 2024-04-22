import streamlit as st
import pickle
import string 

def tranforms(text):  # tranforms means transforms
  text=text.lower()
  text=nltk.word_tokenize(text)
  o=[]
  for i in text:
    if i.isalnum():
      o.append(i)
  text=o[:]
  o.clear()
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      o.append(i)
  text=o[:]
  o.clear()
  for i in text:
    o.append(p.stem(i))

  return " ".join(o)

tf=pickle.load(open('vactorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))
st.title('Email Spam Classifier.rk')

input_mail=st.text_input('Enter the mail')
transformed=tranforms(input_mail)
vec=tf.transform([transformed])
result=model.predict(vec)[0]

if result ==1:
  st.header('SPAM!!')
else:
  st.header('Not SPAM.')

