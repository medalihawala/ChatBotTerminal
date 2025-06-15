import google.generativeai as genai

model = genai.GenerativeModel("gemini-2.0-flash")

API_KEY = "AIzaSyC5lPXppg3l9BVdswfamkCjfYR8HiBpvO4"
genai.configure(api_key=API_KEY)

chat = model.start_chat()

print("chat with Gemini, exit to quit")
while True:
    user_input = input("you : ")
    if user_input.lower() == exit:
        break
    response = chat.send_message(user_input)
    print("Gemini", response.text)