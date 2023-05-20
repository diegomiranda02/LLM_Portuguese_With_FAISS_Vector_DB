from factories.tools_factories import ToolFactory
from tools.report_tools import ToolWhoCreateDocumentOfTCUReport
from tools.report_tools import ToolWhoCreateWorkReportHistory

from models import BERT_portuguese_model_api

tool = ToolWhoCreateDocumentOfTCUReport('Teste');
toolFactory = ToolFactory()
toolFactory.register_tool(ToolWhoCreateDocumentOfTCUReport('Teste').description, ToolWhoCreateDocumentOfTCUReport('Teste'))
toolFactory.register_tool(ToolWhoCreateWorkReportHistory('Teste2').description, ToolWhoCreateWorkReportHistory('Teste2'))
toolFactory.generate_tools_vector_database()

question_one = "Gere um relatorio do TCU do ano de 2022"
question_two = "Gere um relatorio funcional do servidor Diego Miranda de Paula, matricula 12345"

toolOneCalled = toolFactory.get_tool(question_one)
print('toolOneCalled')

toolTwoCalled = toolFactory.get_tool(question_two)
print('toolTwoCalled')

print(BERT_portuguese_model_api.getAnswer(question_one, toolOneCalled.which_year()))

print(BERT_portuguese_model_api.getAnswer(question_two, toolTwoCalled.who_is_the_person()))

