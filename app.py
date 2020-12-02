import streamlit as st
import requests
import collections 
import json
        
    
def main():
    st.title("Find the Distribution of sentence lengths in a file")
    
    url = st.text_input('Url of the book:')
    filename = url.split('/')[-1] #+ '.abc'
    
    if st.button('Submit url'):
        link = 'https://us-central1-faas-297022.cloudfunctions.net/sent_freq'
        param = {'link': url}
        r = requests.post(link, json=param)
        data = json.loads(r.text) #r.text.strip('][').split(', ')
        # print(type(data))
        st.write(dict(collections.Counter(data)))
        st.write(url)
        
        link = 'https://us-central1-faas-297022.cloudfunctions.net/plot_data'
        param = {'data': data, 'filename': filename}
        
        r = requests.post(link, json=param)
        st.image("https://storage.googleapis.com/faasimages/" + filename[:-3] + "png")
        # st.pyplot(json.loads(r.text))
        
        st.write("Done")

if __name__ == "__main__":
    main()