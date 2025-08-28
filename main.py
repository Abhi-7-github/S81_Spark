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
