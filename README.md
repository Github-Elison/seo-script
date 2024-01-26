# Análise de SEO com Python

Este projeto em Python realiza uma análise básica de SEO de um site, examinando várias métricas, incluindo meta tags, contagem de palavras-chave, análise de links internos/externos e a existência de um arquivo `robots.txt`.

## Como Usar

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências:

bash
Copy code
pip install -r requirements.txt
Execute o script:

bash
Copy code
python seo_analyzer.py
Certifique-se de substituir https://www.unibf.com.br/ pelo URL do site que deseja analisar.

Métricas Analisadas
Meta Tags
O script verifica as seguintes meta tags:

Título (<title>): O título da página.
Descrição (<meta name="description">): A descrição da página.
Palavras-chave (<meta name="keywords">): As palavras-chave da página.
Contagem de Palavras-chave
O script conta a frequência das palavras-chave encontradas nas meta tags.

Análise de Links
O script identifica links internos e externos na página.

robots.txt
O script verifica a existência e obtém o conteúdo do arquivo robots.txt se estiver disponível.
