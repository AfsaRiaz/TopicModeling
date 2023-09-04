import streamlit as st
import bertopic
from bertopic import BERTopic

loaded_model = BERTopic.load("BERTopicModel/")

def topic_modeling(input_data):
    predicted_topic, _ = loaded_model.transform(input_data)
    
    if (predicted_topic[0] == 0):
        return "Review about Product Watch"
    elif (predicted_topic[0] == 1):
        return "Review about Product Dress"
    elif (predicted_topic[0] == 2):
        return "Product Quality"
    elif (predicted_topic[0] == 3):
        return "Product Order"
    elif (predicted_topic[0] == 4):
        return "Product Display Picture"
    elif (predicted_topic[0] == 5):
        return "Review about Product Shoes"
    elif (predicted_topic[0] == 6):
        return "Product Color"
    elif (predicted_topic[0] == 7):
        return "Review about Product Shirt"
    else:
        return "Product Size"

def main():
    st.title('Roman Urdu Topic Modeling Web App')
    Review = st.text_input('Enter a Roman Urdu Product Review')
    result = ''
    
    if st.button('Predict Review Topic'):
        result = topic_modeling(Review)

    st.success(result)  
    
if __name__ == '__main__':
    main()      
        
    
    
    
