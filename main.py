
import google.generativeai as genai

# Replace 'your-api-key' with your actual Gemini API key
api_key = 'AIzaSyCUKH9lKuKJufWciMu4p7AD28ATGaO-mmE'
genai.configure(api_key=api_key)

topic = "photosynthesis"
difficulty = "beginner"
prompt = f"Explain the concept of {topic} in simple terms suitable for a {difficulty} level student."

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(prompt)

print("Dynamic Prompt Output:")
print(response.text.strip())