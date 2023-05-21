from factories.tools_factories import ToolFactory
from agents.agent import Agent
from tools.report_tools import *

# Create the tool factory
toolFactory = ToolFactory()
toolFactory.register_tool(ToolWhoCreateDocumentOfTCUReport().description, ToolWhoCreateDocumentOfTCUReport())
toolFactory.register_tool(ToolWhoCreateWorkReportHistory().description, ToolWhoCreateWorkReportHistory())
toolFactory.register_tool(ToolWhoCreateFinancialReport().description, ToolWhoCreateFinancialReport())
toolFactory.generate_tools_vector_database()

command = "Gere um relatorio financeiro no mes de abril e no ano de 2023"
# command = "Gere um relatorio funcional do servidor Diego Miranda de Paula, matricula 12345"

# Getting the tool to execute the command
tool = toolFactory.get_tool(command)

# Starting Agent with the tool to execute the command
agent = Agent(tool)
print(agent.executeCommand(command))



