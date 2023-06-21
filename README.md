# Uma abordagem de como usar LLMs para acessar os sistemas de uma empresa 

As LLMs são utilizadas para várias tarefas, como por exemplo, NER, question answering, geração de textos, sumarização, entre outros usos. Uma das principais vantagens de usar LLM é utilizar a linguagem natural para se comunicar com o sistemas, sem necessariamente aprender as funcionalidades. Isso permite uma facilidade no uso e na capacitação dos funcionários da empresa. 

Neste artigo vou tratar de uma nova forma de utilizar LLM na parte de question answering para possibilitar acessar os sistemas existentes em uma empresa com o menor custo de implantação possível.

Para implementação da solução foi desenvolvido um software em Python para permitir o funcionamento de abordagem proposta. Esse software utiliza os termos agentes e ferramentas que são utilizados no framework Langchain, porém com implementação e conceito distintos. Neste artigo o agente é um componente do software que é responsável por executar um comando solicitado pelo usuário utilizando uma ferramenta e acessando o recurso com a ferramenta. O conceito de ferramenta, neste artigo, é um componente que permite construir o meio de acesso ao recurso que o usuário está solicitando, definindo pra isso os requisitos de uso. Esses requisitos são perguntas cujas repostas formarão os parâmetros para acessar o recurso. O agente é o responsável por completar os requisitos e executar as ferramentas.

O modo tradicional de usar um algoritmo treinado para question answering é converter a pergunta em embedding. Consulta em um banco de dados vetorial qual vetor de texto, ou o vetor de parte do texto, que mais se aproxima do vetor da pergunta. E seleciona a quantidade de vetores mais próximos para gerar a resposta.

 Na abordagem desse artigo, o que difere é que a própria pergunta passa a ser o conteúdo e as perguntas definidas nas ferramentas serão respondidas utilizando a pergunta do usuário como conteúdo. Para exemplificar melhor, supondo que o usuário queira gerar um relatório financeiro para o mês atual e com previsões futuras. O comando (ou a pergunta) poderia ser "Gere um relatório financeiro do mês de abril do ano de 2023 com previsão para os próximos seis meses". Esse texto seria o conteúdo para o qual seriam feitas as perguntas definidas nas ferramentas. Supondo que haja uma ferramenta para tratar da geração dos relatórios financeiros. Desse comando seria gerado um embedding e seria consultado no banco de dados de vetor qual descrição de ferramenta mais se aproxima com esse vetor. A ferramenta com a descrição mais próxima seria retomada. 

O agente responsável por executar o comando solicitaria à ferramenta quais os requisitos para usá-la, que nada mais seria do que perguntas. A mudança de abordagem ocorre nesse momento, o conteúdo é o comando definido pelo usuário e as perguntas seriam as das ferramentas. Por exemplo, "Qual o tipo de relatório financeiro?", "Para qual mês o relatório deverá ser gerado?", "Para qual ano?", "Com previsão?", "Previsão para qual período?".

Com essas perguntas respondidas, a ferramenta compõe a URL e acessa o sistema responsável por gerar o relatório financeiro e devolve a resposta para o usuário. 

A arquitetura do projeto está definida na figura 1. O usuário acessa a aplicação streamlit, que por sua vez acessa a API com a LLM. A pergunta é convertida em embedding e é buscada a ferramenta, através da descrição, que melhor se aproxima para resolver a questão que foi perguntada. Com a ferramenta selecionada, o agente verifica quais são os requisitos para utilizar a ferramenta. Os requisitos são perguntas que serão feitas a LLM para extrair da questão os parâmetros para formar a URL de consulta. Nesse momento é que a abordagem descrita nesse artigo difere do modo tradicional de utilizar os algoritmos de LLM, conforme explicado anteriormente. Com os requisitos preenchidos (podemos também explicar com as perguntas respondidas), o agente executa a ferramenta e recebe os dados e repassa a reposta para o usuário.

FIGURA 1


Para o projeto serão utilizadas as seguintes ferramentas:

- FAISS como banco de dados de vetor;
- Um algoritmo de LLM da Hugging Face para embedding (https://huggingface.co/ricardo-filho/bert-base-portuguese-cased-nli-assin-2)
- Um algoritmo da Hugging Face para Question Answering ([pierreguillou/bert-base-cased-squad-v1.1-portuguese](https://huggingface.co/pierreguillou/bert-base-cased-squad-v1.1-portuguese))
- Um projeto desenvolvido em Python para possibilitar a implementação da abordagem descrito nesse artigo.
- Uma interface em Streamlit para acesso do usuário (Código fonte em https://github.com/diegomiranda02/frontend_LLM_Project)
- Um serviço web para disponibilizar os endpoints que fornecerão os acessos aos sistemas (Código fonte em https://github.com/diegomiranda02/python_api_server)

Um ponto importante para esclarecer é que foram utilizados dois algoritmos de LLMs, um para embedding e outro para question answering, mas é possível utilizar somente um para os dois propósitos. A intenção foi mostrar que é possível combinar mais de um algoritmo nessa solução.

Uma vantagem dessa solução é que pode-se usar algoritmos que rodam em CPU, barateando o custo, open source e gratuitos, como também programar as ferramentas para acessar qualquer API dos sistemas já existentes na empresa. Gerando a possibilidade de utilizar comandos em linguagem natural para acessar as funcionalidades dos sistemas, diminuindo a necessidade de treinamento de pessoal para aprender a usar os sistemas.

O exemplo para demonstrar a utilização do projeto na prática é a solicitação de um relatório financeiro em determinado mês e determinado ano. Conforme figura abaixo:

![Passo a passo do uso do framework 1 (1)](https://github.com/diegomiranda02/LLM_Portuguese_With_FAISS_Vector_DB/assets/9868024/492cf05e-4f21-4912-85ff-4e53d3f04d3e)

# Para executar o programa siga os seguintes passos:

1 - Instalar as dependências descritas no arquivo environment.yml (Neste exemplo foi utilizado o software Anaconda)
2 - Baixar o projeto https://github.com/diegomiranda02/python_api_server e executar em uma porta distinta das que já estão sendo utilizadas por outros serviços. IMPORTANTE: A porta definida ao executar o serviço deverá ser a mesma utilizada para informar às ferramentas qual URL acessar.
3 - Executar o serviço API server do projeto anterior
4 - No projeto atual executar o python3 main_CONSOLE.py para executar no console.

Caso deseje utilizar uma interface web, siga o dois passos a seguir:
1 - Baixe o projeto https://github.com/diegomiranda02/frontend_LLM_Project e execute a aplicação em Streamlit
2 - No projeto atual executar o python3 main.py para executar o serviço FAST API que será consumido pela aplicação Streamlit.

A implementação feita nesse artigo foi para demonstrar que é possivel utilizar LLMs com um custo mais baixo, acessando as funcionalidades dos sistemas já existentes nas empresas. Nessa solução não foram implementadas a segurança, a autenticação e a autorização de acesso aos dados. Para implantar em produção, todos esses detalhes precisam ser avaliados de acordo com a necessidade do projeto.

