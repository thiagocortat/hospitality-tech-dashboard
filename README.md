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
- Nova seção **Últimas do Mercado** mostrando feed de notícias resumidas
  das últimas duas semanas com busca e filtros por data e empresa.

## Instalação

1. Clone este repositório.
2. Crie um ambiente virtual com `python -m venv .venv` e ative-o.
3. Instale as dependências com `pip install -r requirements.txt`.

## Como executar

Após instalar as dependências, execute o comando abaixo para iniciar o
agendador e abrir o painel interativo em seu navegador padrão:

```bash
python -m hospitality_agent.app
```

## Testes

Rodar `pytest -q` permite validar eventuais testes adicionados ao
projeto.
