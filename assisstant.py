# from openai import OpenAI
# client = OpenAI(api_key="sk-y4G_tgb1WZD2E4MHV1wrHQZcA3hyzDvCEhz6yE1noAT3BlbkFJzSssCQ2HiUb0d22CZslxhkBOC-O-K2sMLlBQ_qxBQA")

# assistant = client.beta.assistants.create(
#   name="Patent Attorney",
#   instructions="You are a patent attorney. Describe it based on your profession",
#   tools=[{"type": "file_search"}],
# tool_resources={"file_search": {"vector_store_ids": ["vs_Urp7JZYqkzWueu4ko7iQ9OJk"]}},
#   model="gpt-4o-mini",
# )



# run = client.beta.threads.create_and_run(
#   assistant_id="asst_gvPFrmBTLFQ7H9ACHyo2IlsC",
#   thread={
#     "messages": [
#       {"role": "user", "content": "Explain the contents of the file."}
#     ]
#   }
# )

# print(run)


# print(assistant)


# empty_thread = client.beta.threads.create()
# print(empty_thread)
# thread_6ZsVsGAYcR2R38r9t0F7H9G6




from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="sk-y4G_tgb1WZD2E4MHV1wrHQZcA3hyzDvCEhz6yE1noAT3BlbkFJzSssCQ2HiUb0d22CZslxhkBOC-O-K2sMLlBQ_qxBQA")

def create_assistant():
    assistant = client.beta.assistants.create(
        name="Patent Attorney",
        instructions="You are a patent attorney. Describe it based on your profession",
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": ["vs_Urp7JZYqkzWueu4ko7iQ9OJk"]}},
        model="gpt-4o-mini"
    )
    return assistant

def create_thread():
    # Create a Thread without passing assistant_id
    thread = client.beta.threads.create()
    return thread

def message(initial_message, thread_id):
    # Create a message in the specified thread
    thread_message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=initial_message,
        # Include the assistant_id in the request
    )
    return thread_message

def get_response(thread_id, message_id):
    # Retrieve the Assistant's response
    message = client.beta.threads.messages.retrieve(
        thread_id=thread_id,
        message_id=message_id
    )
    return message.content

def chat_with_assistant():
    # Step 1: Create an assistant
    assistant = create_assistant()
    assistant_id = assistant.id

    # Step 2: Start a conversation with an initial message
    initial_message = "Hello, how are you?"
    thread = create_thread()
    thread_id = thread.id
    message_response = message(initial_message, thread_id)
    message_id = message_response.id
    response = get_response(thread_id, message_id)
    print(f"Assistant: {response}")

    # Step 3: Continue the conversation in a loop

if __name__ == "__main__":
    chat_with_assistant()
