# Uma abordagem de como usar LLMs para acessar os sistemas de uma empresa

## Introdução

As Linguagens de Modelos de Linguagem (LLMs) têm desempenhado um papel revolucionário em uma variedade de tarefas, incluindo Reconhecimento de Entidades (NER), Respostas a Perguntas, Geração de Texto e Sumarização. Uma das principais vantagens desses modelos é a capacidade de se comunicar com sistemas utilizando linguagem natural, eliminando a necessidade de aprender intricadas funcionalidades. Essa abordagem simplificada não apenas torna o uso mais fácil, mas também agiliza a capacitação dos funcionários dentro de uma empresa.

Neste artigo, exploraremos uma abordagem inovadora para o uso de LLMs, focada na área de Respostas a Perguntas (Question Answering), com o objetivo de acessar sistemas empresariais com custos mínimos de implantação. Para realizar essa implementação, desenvolvemos um software em Python que viabiliza essa abordagem.

## A Base da Solução

Nossa solução se baseia na criação de um software que opera com dois componentes essenciais: Agentes e Ferramentas. Essa estrutura é semelhante à do framework Langchain, embora com implementação e conceitos distintos. Neste contexto, um agente é um componente do software encarregado de executar comandos solicitados pelo usuário, utilizando uma ferramenta específica para acessar um recurso. A ferramenta, por sua vez, é um componente que permite construir a interface de acesso ao recurso desejado, definindo requisitos de uso sob a forma de perguntas cujas respostas serão utilizadas como parâmetros para acessar o recurso. O agente é responsável por coletar as respostas a essas perguntas e executar as ferramentas.

## Superando Desafios: Utilizando Algoritmos Prontos e CPUs

Um dos desafios fundamentais enfrentados durante o desenvolvimento deste projeto era a necessidade de utilizar algoritmos de LLM já treinados e disponíveis na Hugging Face sem a necessidade de realizar o fine-tuning. Isso se mostrou crucial para manter os custos baixos, uma vez que o treinamento personalizado de modelos de LLM pode ser computacionalmente intensivo e caro.

Além disso, outro aspecto importante foi a escolha de executar o sistema em CPUs convencionais, em vez de GPUs ou TPUs mais caras. Essa escolha não apenas reduziu significativamente os custos operacionais, mas também tornou a solução acessível e viável para pequenas e microempresas, que geralmente têm recursos limitados para investir em infraestrutura de hardware sofisticada.

Assim, nosso projeto destaca a capacidade de aproveitar algoritmos de LLM pré-treinados e a execução em CPUs comuns, tornando-o uma solução econômica e eficaz que pode ser facilmente implementada em empresas de todos os tamanhos. Essa abordagem inovadora democratiza o acesso à tecnologia avançada, permitindo que até mesmo as pequenas empresas aproveitem os benefícios das LLMs para aprimorar suas operações e processos.

## Abordagem Tradicional vs. Abordagem Inovadora

Na abordagem tradicional de Respostas a Perguntas com LLMs, as perguntas dos usuários são convertidas em representações numéricas chamadas embeddings. Esses embeddings são então comparados com vetores de texto ou partes de texto em um banco de dados vetorial para encontrar a resposta apropriada.

Em nossa abordagem inovadora, a pergunta do usuário se torna o conteúdo, e as perguntas definidas nas ferramentas são respondidas usando a pergunta do usuário como base. Por exemplo, se um usuário desejar gerar um relatório financeiro para o mês atual com previsões futuras, o comando ou pergunta pode ser: "Gere um relatório financeiro para abril de 2023 com previsões para os próximos seis meses." Nesse caso, esse texto se tornaria o conteúdo para o qual as perguntas definidas nas ferramentas seriam direcionadas.

Suponhamos que exista uma ferramenta específica para a geração de relatórios financeiros. A partir do comando do usuário, um embedding é gerado e consultado no banco de dados vetorial para encontrar a descrição da ferramenta que mais se assemelha a esse vetor. O agente, responsável por executar o comando, solicitaria à ferramenta os requisitos para seu uso, que nada mais são do que uma série de perguntas. A mudança de abordagem ocorre aqui: o conteúdo é o comando definido pelo usuário, e as perguntas são provenientes das ferramentas. Exemplos de perguntas incluiriam: "Qual é o tipo de relatório financeiro?", "Para qual mês o relatório deve ser gerado?", "Para qual ano?", "Com previsões?", "Previsões para qual período?".

Uma vez que essas perguntas são respondidas, a ferramenta compõe a URL e acessa o sistema responsável pela geração do relatório financeiro, retornando a resposta ao usuário.

## Arquitetura do Projeto

A arquitetura do projeto é ilustrada na Figura 1. O usuário acessa a aplicação Streamlit, que, por sua vez, se conecta à API com o LLM. A pergunta do usuário é convertida em um embedding, e a ferramenta mais apropriada é selecionada com base na descrição. O agente então verifica os requisitos para o uso da ferramenta, que são essencialmente perguntas que extrairão os parâmetros da pergunta do usuário para formar a URL de consulta. É aqui que nossa abordagem difere da maneira tradicional de usar algoritmos de LLM, como explicado anteriormente. Com os requisitos preenchidos (ou seja, as perguntas respondidas), o agente executa a ferramenta e recebe os dados, que são posteriormente repassados ao usuário.

## Ferramentas Utilizadas no Projeto

Para a implementação do projeto, foram utilizadas as seguintes ferramentas:

FAISS como banco de dados de vetor.
Um algoritmo de LLM da Hugging Face para embedding (ricardo-filho/bert-base-portuguese-cased-nli-assin-2).
Um algoritmo da Hugging Face para Question Answering (pierreguillou/bert-base-cased-squad-v1.1-portuguese).
Um projeto desenvolvido em Python que permite a implementação da abordagem descrita neste artigo.
Uma interface em Streamlit para acesso do usuário (Código fonte em frontend_LLM_Project).
Um serviço web para disponibilizar os endpoints que fornecerão os acessos aos sistemas (Código fonte em python_api_server).
É importante ressaltar que utilizamos dois algoritmos de LLMs, um para embedding e outro para question answering, como exemplo, mas é possível utilizar apenas um algoritmo para ambas as finalidades. A intenção era demonstrar a possibilidade de combinar mais de um algoritmo nessa solução.

## Vantagens da Solução

Uma das vantagens mais significativas dessa abordagem é a capacidade de utilizar algoritmos que podem ser executados em CPUs, o que reduz custos operacionais. Além disso, a solução é de código aberto e gratuita, permitindo a programação de ferramentas personalizadas para acessar qualquer API dos sistemas já existentes na empresa. Isso abre possibilidades para utilizar comandos em linguagem natural para acessar funcionalidades dos sistemas, diminuindo a necessidade de treinamento de pessoal para aprender a usar esses sistemas.

Exemplo de Utilização

Para ilustrar o uso prático do projeto, considere o cenário em que um usuário solicita a geração de um relatório financeiro para um mês e ano específ
