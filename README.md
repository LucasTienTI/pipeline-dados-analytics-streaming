# Pipeline de Dados End-to-End & Dashboard de Analytics - Streaming

Este projeto demonstra a construção de um pipeline de dados completo (End-to-End) simulando o ambiente de uma plataforma de streaming (estilo Netflix), integrando geração de dados, banco de dados relacional e inteligência de negócios.

## 🛠️ Tecnologias Utilizadas
* **Python**: Geração dos dados sintéticos e automação da carga (`pandas`, `faker`, `sqlalchemy`).
* **PostgreSQL**: Armazenamento e modelagem do banco de dados relacional (Tabelas Fato e Dimensão).
* **SQL**: Criação de queries de visualização e validação dos dados.
* **Power BI**: Desenvolvimento de Dashboard Executivo para análise de engajamento e métricas de consumo.

## 📐 Arquitetura do Projeto
1. **Ingestão**: Scripts em Python simulam e estruturam os dados brutos de usuários e histórico de consumo.
2. **Carga (ETL)**: O script Python conecta ao PostgreSQL e envia os dados para o banco local.
3. **Modelagem SQL**: Estruturação das tabelas no pgAdmin para otimizar as consultas.
4. **Visualização**: Conexão do Power BI ao banco de dados para extração de insights em tempo real.
 
  
  ## 📊 Visualização do Dashboard
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9d23141e-c2fa-40ab-ba9e-2a3eebd40ea4" />
