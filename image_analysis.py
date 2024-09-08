import requests
from openai import OpenAI

def fetch_data_from_api(api_url):
    """Fetch image URLs and text content from the given API."""
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    
    # Extract image URLs and text content from the API response
    image_urls = [image['url'] for image in data.get('images', [])]
    text_contents = [text['content'] for text in data.get('texts', [])]
    
    return image_urls, text_contents

def generate_messages(image_urls, text_contents):
    """Generate message payloads for OpenAI API, sending each text and image URL with type as separate messages."""
    messages = [
        {
            "role": "user",
            "content": "You are a patent attorney. Can you summarize images and text separately?",
            "type": "text"
        },
         {
            "role": "user",
            "content": [ 
                {
                "type": "text",
                 "text": content
                }for content in text_contents
            ]
        } ,
        {
             "role": "user",
            "content": [
                {
                "type": "image_url",
                "image_url": {
                "url": url
            },
            "detail":"low"
        } for url in image_urls
    ]
}
    ]
    
    # Add text contents with type
   
    
 
 
    return messages

def main():
    # API URL to get image URLs and text content
    api_url = "http://localhost:8081/api/disclosurecontents?docket_number=d112"
    
    # Fetch image URLs and text content
    image_urls, text_contents = fetch_data_from_api(api_url)
    
    # Initialize OpenAI client with your API key
    client = OpenAI(api_key='your-openai-api-key')
    
    # Prepare the initial messages for the OpenAI API
    print('hello world')
    messages = generate_messages(image_urls, text_contents)
    print("message :", messages)
    # Prepare the request to OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=4096,
    )
    
    # Print the initial response
    print("Response Content:", response.choices[0].message.content)
    print("Total tokens used:", response.usage.total_tokens)
    print("Prompt tokens:", response.usage.prompt_tokens)
    print("Completion tokens:", response.usage.completion_tokens)

    # Continue the conversation interactively
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        # Add user input to the messages
        messages.append({"role": "user", "content": user_input, "type": "text"})
        
        # Get response from the assistant
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=16384,
        )
        
        # Print assistant's response
        assistant_response = response.choices[0].message.content
        print(f"Assistant: {assistant_response}")
        
        # Append assistant response to messages for context continuity
        messages.append({"role": "assistant", "content": assistant_response, "type": "text"})

if __name__ == "__main__":
    main()
