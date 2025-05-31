# Packages : pip install langchain langchain-cohere cohere
# pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
# pip install --upgrade langchain

import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_cohere import ChatCohere

# Set API Key in environment (optional if already set in shell)
os.environ["COHERE_API_KEY"] = "o6DdGd0awe4vhcOEBS4r3RJOt0PdNB4iC60lIE40"

# Load your file
file_path = '/Users/sooryakumar/PYTHON/text1.txt'
with open(file_path, 'r') as file:
    document_text = file.read()

# Initialize Cohere Chat LLM (no args needed if env var is set)
llm = ChatCohere()

# Define prompt
prompt = PromptTemplate(
    input_variables=["document"],
    template="""
You are a helpful assistant.
Given the following document, summarize it in **bullet points**:
---
{document}
---
Summary:
"""
)

# Build LangChain pipeline
chain = prompt | llm | StrOutputParser()

# Run chain
response = chain.invoke({"document": document_text})

# Show result
print(response)
