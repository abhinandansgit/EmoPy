import google.generativeai as genai
genai.configure(api_key='**************************')
model = genai.GenerativeModel('gemini-pro')
def get_sentiment(text):
       return 'neutral'
def chatbot_response(user_input):
    sentiment = get_sentiment(user_input)
    chat = model.start_chat(history=[])
    response = chat.send_message(user_input, stream=True)
    full_text = ''
    for chunk in response:
      if chunk.text:
          full_text += chunk.text
    if sentiment == 'positive':
      print(f"Chatbot (Positive): {full_text}")
    elif sentiment == 'negative':
      print(f"Chatbot (Negative): {full_text}")
    else:
      print(f"Chatbot (Neutral): {full_text}")

if __name__ == "__main__":
    user_input = input("Welcome to the EmoPy Emotional Intelligence by Abhinandan!\n Ask me anything: ")
    chatbot_response(user_input)
