from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

#guardRails evaluating LLM + LLM observability

from system_prompts import ROUTER_AGENT_SYSTEM_PROMPT, NEWS_AGENT_PROMPT, SCAM_PROMPT

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini-2025-04-14") #smartest non-reasoning model

def router_agent(state):

    prompt = ChatPromptTemplate.from_messages([
        ("system" , ROUTER_AGENT_SYSTEM_PROMPT),
        ("human" , "{input}")
    ])

    routing_chain = prompt | llm
    agent_category = routing_chain.invoke({"input" : state["input"]})

    return {"route" : agent_category.content}

def scam_agent(state):

    prompt = ChatPromptTemplate.from_messages([
        ("system", SCAM_PROMPT),
        ("human", "{input}")
    ])

    routing_chain = prompt | llm
    scam_response = routing_chain.invoke({"input": state["input"]})

    return {"response": scam_response.content}

def news_agent(state):
    web_search_tool = TavilySearch(max_results=5)

    agent = create_agent(
        model=llm,
        system_prompt=NEWS_AGENT_PROMPT,
        tools=[web_search_tool]
    )

    result = agent.invoke({
        "messages" : [
            {
                "role" : "user",
                "content" : state["input"]
            }
        ]
    }
    )

    return {"response" : result["messages"][-1].content}




