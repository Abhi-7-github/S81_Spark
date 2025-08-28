"""
One-Shot Prompting Example

One-shot prompting is when you provide the AI with a single example of the task you want it to perform, along with your instruction. This helps the model understand the format and style you expect in its response.
"""

import google.generativeai as genai

# Replace 'your-api-key' with your actual Gemini API key
api_key = 'your-api-key'
genai.configure(api_key=api_key)

one_shot_prompt = (
    "Summarize the following article in three bullet points.\n\n"
    "Example:\n"
    "Article: The sun is a star at the center of our solar system. It provides light and heat to Earth.\n"
    "Summary:\n"
    "- The sun is a star.\n"
    "- It is at the center of our solar system.\n"
    "- It provides light and heat to Earth.\n\n"
    "Now summarize this article:\n"
    "Artificial intelligence is transforming education by personalizing learning experiences, automating administrative tasks, and providing intelligent tutoring systems. It enables educators to focus more on student engagement and less on routine work. As AI continues to evolve, its impact on education is expected to grow even further."
)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(one_shot_prompt)

print("One-Shot Prompt Output:")
print(response.text.strip())
"""
RTFC Framework Example for Spark AI

Role: Spark, an AI-powered personalized learning companion
Task: Provide clear, engaging, and age-appropriate explanations for any educational topic
Format: Structured JSON with fields: topic, explanation, key_points (list of 3)
Constraints: Explanations must be concise, suitable for a beginner, and limited to 3 key points
"""

import google.generativeai as genai

# System prompt (RTFC)
system_prompt = (
    "You are Spark, an AI-powered personalized learning companion. "
    "Your task is to provide clear, engaging, and age-appropriate explanations for any educational topic the user requests. "
    "Always respond in structured JSON format with the following fields: 'topic', 'explanation', and 'key_points' (a list of 3 key points). "
    "Keep explanations concise and suitable for a beginner student."
)

# User prompt (RTFC)
topic = "photosynthesis"
difficulty = "beginner"
user_prompt = f"Explain the concept of {topic} for a {difficulty} student."

# Combine system and user prompts for the AI call
prompt = f"{system_prompt}\nUser: {user_prompt}"

# Replace 'your-api-key' with your actual Gemini API key
api_key = 'AIzaSyCUKH9lKuKJufWciMu4p7AD28ATGaO-mmE'
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(prompt, generation_config={"top_k": 40})

print("RTFC Structured Output:")
print(response.text.strip())

# Log the number of tokens used (input + output)
if hasattr(response, 'usage_metadata'):
    total_tokens = response.usage_metadata.get('total_tokens')
    prompt_tokens = response.usage_metadata.get('prompt_token_count')
    candidates_tokens = response.usage_metadata.get('candidates_token_count')
    print(f"Total tokens used: {total_tokens}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {candidates_tokens}")
else:
    print("Token usage information not available for this response.")

