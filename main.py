# fastapi libraries
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

# Project libraries
from factories.tools_factories import ToolFactory
from agents.agent import Agent
from tools.report_tools import *

# Create the tool factory
toolFactory = ToolFactory()
toolFactory.register_tool(ToolWhoCreateDocumentOfTCUReport().description, ToolWhoCreateDocumentOfTCUReport())
toolFactory.register_tool(ToolWhoCreateWorkReportHistory().description, ToolWhoCreateWorkReportHistory())
toolFactory.register_tool(ToolWhoCreateFinancialReport().description, ToolWhoCreateFinancialReport())
toolFactory.register_tool(ToolWhichCreatesAReportOfTheMostSoldProducts().description, ToolWhichCreatesAReportOfTheMostSoldProducts())
toolFactory.generate_tools_vector_database()

# Instantiate the API
app = FastAPI()

# Decide who can access te API
origins = [
    "http://localhost",
    "http://localhost:8501"
]

# Insert the access permissions in the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check if the API is Alive
@app.get("/", response_class=PlainTextResponse)
async def root():
    return "API is Alive"

# Return an Answer for a Question, based on the content
@app.get("/llm_api", response_class=PlainTextResponse)
async def answer(command: str):
    # Getting the tool to execute the command
    tool = toolFactory.get_tool(command)

    # Starting Agent with the tool to execute the command
    agent = Agent(tool)
    result = agent.executeCommand(command)
    return result






