SYSTEM_MESSAGE = """A history of conversations between an AI assistant and the user, plus the last user's message, is given to you.

In addition, you have access to a list of available tools. Each tool is a function that requires a set of parameters and, in response, returns information that the AI assistant needs to provide a proper answer.

The list of tools is a JSON list, with each tool having a name, a description to help you identify which tool might be needed, and "parameters," which is a JSON schema to explain what parameters the tool needs, and you have to extract their value from the user's last message.

Depending on the user's question, the AI assistant can either directly answer the user's question without using a tool, or it may need to first call one or multiple tools, wait for the answer, then aggregate all the answers and provide the final answer to the user's last questions.

Your job is to closely check the user's last message and the history of the conversation, then decide if the AI assistant needs to answer the question using any tools. You also need to extract the values for the tools that you think the AI assistant needs. Remember you can select multiple tools if needed.

You should think step by step, provide your reasoning for your response, then add the JSON response at the end following the below schema:

{
    "tool_calls" : [
        { 
            "name": "function_name_1",
            "arguments": {
                "arg1" : "value1", "arg2": "value2", ...
            }
        },
        { 
            "name": "function_name_2",
            "arguments": {
                "arg1" : "value1", "arg2": "value2", ...
            }
        }, ...
    ]
}

** If no tools are required, then return an empty list for "tool_calls". **

**Wrap the JSON response between ```json and ```**. 

**Whenever a message starts with 'SYSTEM MESSAGE', that is a guide and help information for you to generate your next response, do not consider them a message from the user, and do not reply to them at all. Just use the information and continue your conversation with the user.**"""

CLEAN_UP_MESSAGE = "When I tried to extract the content between ```json and ``` and parse the content to valid JSON object, I faced with the abovr error. Remember, you are supposed to wrap the schema between ```json and ```, and do this only one time. First find out what went wrong, that I couldn't extract the JSON between ```json and ```, and also faced error when trying to parse it, then regenerate the your last message and fix the issue."
SUFFIX = """Think step by step and justify your response. Make sure to not miss in case to answer user query we need multiple tools, in that case detect all that we need, then generate a JSON response wrapped between "```json" and "```". Remember to USE THIS JSON WRAPPER ONLY ONE TIME."""


def get_func_result_guide(function_call_result : str) -> str:
    return f"SYSTEM MESSAGE: \n```json\n{function_call_result}\n```\n\nThe above is the result after functions are called. Use the result to answer the user's last question.\n\n"