


"""
Structured Output in LLMs:

Structured output is when you instruct the AI model to return its response in a specific format, such as JSON or a table, making it easier to parse and use programmatically. This is useful for extracting key information or integrating with other systems.
"""

import google.generativeai as genai

# Replace 'your-api-key' with your actual Gemini API key
api_key = 'AIzaSyCUKH9lKuKJufWciMu4p7AD28ATGaO-mmE'
genai.configure(api_key=api_key)


topic = "photosynthesis"
difficulty = "beginner"
prompt = (
		f"""
		Provide a structured JSON output with the following fields:
		- topic: the topic explained
		- explanation: a simple explanation suitable for a {difficulty} level student
		- key_points: a list of 3 key points about the topic
		Example output:
		{{
			"topic": "...",
			"explanation": "...",
			"key_points": ["...", "...", "..."]
		}}
		Now, use the topic: {topic}
		"""
)



model = genai.GenerativeModel('gemini-pro')
# Set top_k to 40 for sampling from the top 40 most likely tokens
response = model.generate_content(prompt, generation_config={"top_k": 40})


print("Structured Output:")
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
	