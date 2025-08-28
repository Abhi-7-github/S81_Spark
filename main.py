import google.generativeai as genai

"""
Embeddings in LLMs:

Embeddings are numerical vector representations of text, computed by LLMs to capture semantic meaning. They allow comparison of text similarity, clustering, search, and more. Embeddings are computed by passing text to a model's embedding endpoint, which returns a high-dimensional vector. Practical applications include semantic search, recommendation, and clustering.
"""

def get_text_embedding(text):
    """Generate an embedding vector for the given text using Gemini API."""
    embedding_model = genai.GenerativeModel('embedding-001')
    embedding_response = embedding_model.embed_content(text)
    return embedding_response['embedding'] if 'embedding' in embedding_response else None

# Replace 'your-api-key' with your actual Gemini API key
api_key = 'AIzaSyCUKH9lKuKJufWciMu4p7AD28ATGaO-mmE'
genai.configure(api_key=api_key)

topic = "photosynthesis"
difficulty = "beginner"

# Example: Generate and print embedding for the topic
embedding = get_text_embedding(topic)
print("\nEmbedding vector for topic:")
print(embedding)

"""
Structured Output in LLMs:

Structured output is when you instruct the AI model to return its response in a specific format, such as JSON or a table, making it easier to parse and use programmatically. This is useful for extracting key information or integrating with other systems.
"""

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
