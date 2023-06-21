from factories.tools_factories import ToolFactory
from agents.agent import Agent
from tools.report_tools import *

# Create the tool factory
toolFactory = ToolFactory()
toolFactory.register_tool(ToolWhoCreateDocumentOfTCUReport().description, ToolWhoCreateDocumentOfTCUReport())
toolFactory.register_tool(ToolWhoCreateWorkReportHistory().description, ToolWhoCreateWorkReportHistory())
toolFactory.register_tool(ToolWhoCreateFinancialReport().description, ToolWhoCreateFinancialReport())
toolFactory.register_tool(ToolWhichCreatesAReportOfTheMostSoldProducts().description, ToolWhichCreatesAReportOfTheMostSoldProducts())
toolFactory.register_tool(ToolWhichAddNewEmployent().description, ToolWhichAddNewEmployent())
toolFactory.generate_tools_vector_database()

# command = "Gere um relatorio financeiro do mes de abril e no ano de 2023"
command = "Cadastre o funcionario Diego Miranda de Paula, CPF 11111111, RG 1234412334, emitida em 02/02/2202 por SSP/RN, residente à Rua Teste de Rua Natal da Silva, numero 1234, apt 500000, torre 199191919, condominio teste teste teste, bairro nova parnamirim, cep 1212122112, no estado do Rio Grande do Norte. Com salario de R$ 400,00 por mês, carga horaria de 40 horas semanais, 8 horas por dia, regime de contratacao CLT."

# Getting the tool to execute the command
tool = toolFactory.get_tool(command)

# Starting Agent with the tool to execute the command
agent = Agent(tool)
print(agent.executeCommand(command))



