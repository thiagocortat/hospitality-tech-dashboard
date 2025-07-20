# Hospitality Tech Dashboard

Este repositório contém um exemplo de implementação de um agente de IA
chamado **Hospitality Market Intelligence**. O agente executa coletas
diárias de notícias em fontes abertas do setor de tecnologia para
hotelaria e apresenta insights em um painel interativo.

## Principais recursos

- Coleta de notícias a partir de sites públicos utilizando `requests` e
  `BeautifulSoup`;
- Classificação simples do conteúdo em categorias como atualizações de
  produto, fusões e aquisições e parcerias;
- Agendamento diário com a biblioteca `schedule`;
- Painel construído com `streamlit` exibindo contagem de menções por
  empresa e tópicos por categoria.

Execute `python -m hospitality_agent.app` para iniciar o scheduler e o
painel (necessário possuir as dependências do `requirements.txt`).
