from langchain_groq import ChatGroq

from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode,tools_condition
from tools.sales_tools import sales_tools
from langgraph.graph import StateGraph,START,END
from typing import Annotated,List

from langgraph.graph.message import add_messages

from langchain_core.prompts import ChatPromptTemplate,HumanMessagePromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,ToolMessage

from pydantic import BaseModel

load_dotenv()

model=ChatGroq(
    model="openai/gpt-oss-120b"
    )
print(" model created succesfullly ! ")



# llm with tools 

llm_with_tools=model.bind_tools(sales_tools)
print("Tool binded succesfully ! ")

# response = llm_with_tools.invoke(
#     "What is the price of Kaju Katli?"
# )
# print(response)

# # graph building 

# for tool in product_tools:
#     print(tool.name)



class ProductState(BaseModel):
    messages:Annotated[List,add_messages]


def chatNode(state: ProductState):
    print("chatNode Working ! ")

    prompt = ChatPromptTemplate.from_messages([
        ("system", """
            You are a Product Agent.

            you are giving wrong  tool naming double check the tool name 
            Use the available product tools to answer customer queries with correct wording.
            Select the appropriate registered tool.
            Never invent tool names or arguments.
            Do not hallucinate product information.
            If customer misspelled item . don't tell to user.
        """),
        ("placeholder", "{messages}")
    ])

    chain = prompt | llm_with_tools

    response = chain.invoke({
        "messages": state.messages
    })

    return {"messages": [response]}

builder=StateGraph(ProductState)
builder.add_node("chatNode",chatNode)
builder.add_node("tools",ToolNode(sales_tools))
builder.add_edge(START,"chatNode")
builder.add_conditional_edges("chatNode",tools_condition)
builder.add_edge('tools',"chatNode")


product_agent= builder.compile()

# from IPython.display import Image, display

# png_data = product_agent.get_graph().draw_mermaid_png()

# with open("product_agent.png", "wb") as file:
#     file.write(png_data)


while True:
    query=input()
    if query=="break":
        break
    final_response = product_agent.invoke({
        "messages": [
            HumanMessage(content=query)
        ]
    })


    print(final_response["messages"][-1].content)


    for message in final_response["messages"]:
        if isinstance(message, ToolMessage):
            print("\n--- TOOL MESSAGE ---")
            print("Tool Name:", message.name)
            print("Content:", repr(message.content))
        if isinstance(message, SystemMessage):
            print("\n--- System MESSAGE ---")
            print("Tool Name:", message.name)
            print("Content:", repr(message.content))
        if isinstance(message, HumanMessage):
            print("\n--- Human MESSAGE ---")
            print("Tool Name:", message.name)
            print("Content:", repr(message.content))

    # Your existing prompt and chain