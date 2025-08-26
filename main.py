import google.generativeai as genai

# Replace 'your-api-key' with your actual Gemini API key
api_key = 'AIzaSyA5zRQif_COG9DhqDrqIiXKkzCYu8FVJdM'
genai.configure(api_key=api_key)

topic = "photosynthesis"
difficulty = "beginner"
prompt = f"Explain the concept of {topic} in simple terms suitable for a {difficulty} level student."

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(prompt)

print("Dynamic Prompt Output:")
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