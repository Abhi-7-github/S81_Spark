
"""
Top P (nucleus sampling) in LLMs:

Top P is a parameter that controls the diversity of AI-generated responses. It sets a probability threshold so the model only considers the smallest set of most likely next words whose cumulative probability exceeds Top P. Lower values make output more focused; higher values make it more creative.
"""

import google.generativeai as genai

# Replace 'your-api-key' with your actual Gemini API key
api_key = 'AIzaSyCUKH9lKuKJufWciMu4p7AD28ATGaO-mmE'
genai.configure(api_key=api_key)

topic = "photosynthesis"
difficulty = "beginner"
prompt = f"Explain the concept of {topic} in simple terms suitable for a {difficulty} level student."

model = genai.GenerativeModel('gemini-pro')
# Set top_p to 0.7 for nucleus sampling
response = model.generate_content(prompt, generation_config={"top_p": 0.7})

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