
"""
Temperature in LLMs:

Temperature is a parameter that controls the randomness of AI-generated responses. Lower values (close to 0) make the output more focused and deterministic, while higher values (up to 1) make it more creative and diverse.
"""

import google.generativeai as genai

# Replace 'your-api-key' with your actual Gemini API key
api_key = 'AIzaSyCUKH9lKuKJufWciMu4p7AD28ATGaO-mmE'
genai.configure(api_key=api_key)

topic = "photosynthesis"
difficulty = "beginner"
prompt = f"Explain the concept of {topic} in simple terms suitable for a {difficulty} level student."

model = genai.GenerativeModel('gemini-pro')
# Set temperature to 0.8 for more creative output
response = model.generate_content(prompt, generation_config={"temperature": 0.8})

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