from langflow.load import run_flow_from_json

# Define the tweaks for the flow
TWEAKS = {
    "ChatInput-KVAeE": {},
    "ChatOutput-F6j5v": {},
    "OllamaModel-XbfzQ": {},
    "Prompt-iZmsD": {},
    "Chroma-GQFow": {},
    "File-bDFWg": {},
    "RecursiveCharacterTextSplitter-pzEks": {},
    "OllamaEmbeddings-bCQKU": {},
    "Chroma-SpfSz": {},
    "ParseData-w9AfR": {}
}

# Define the special command to terminate the loop
TERMINATION_COMMAND = "exit"

while True:
    # Get input from the user
    input_text = input("You: ")
    
    # Check if the user wants to exit
    if input_text.lower() == TERMINATION_COMMAND:
        print("Exiting the chatbot. Goodbye!")
        break
    
    # Run the flow with the input text
    result = run_flow_from_json(
        flow="chatbot.json",
        input_value=input_text,
        session_id="",  # provide a session id if you want to use session state
        fallback_to_env_vars=True,  # False by default
        tweaks=TWEAKS
    )
    
    # Extract and print the response message
    data = result[0].outputs
    message = data[0].results['message']
    print(f"Bot: {message.text}")