
import google.generativeai as genai

# Replace 'your-api-key' with your actual Gemini API key
api_key = 'AIzaSyCUKH9lKuKJufWciMu4p7AD28ATGaO-mmE'
genai.configure(api_key=api_key)

prompt = (
    "Summarize the following article in three bullet points:\n"
    "Artificial intelligence is transforming education by personalizing learning experiences, "
    "automating administrative tasks, and providing intelligent tutoring systems. "
    "It enables educators to focus more on student engagement and less on routine work. "
    "As AI continues to evolve, its impact on education is expected to grow even further."
)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(prompt)

print("Zero-Shot Prompt Output:")
print(response.text.strip())