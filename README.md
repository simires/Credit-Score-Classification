# Credit-Score-Classification
Projeto final do Bootcamp [RE]Start – Trilha de Cientista de Dados promovido pelo Data Girls

## Objetivo do Projeto
- Desenvolver um modelo de classificação supervisionada capaz de prever a categoria de score de crédito de um cliente (**Poor**, **Standard** ou **Good**) com base em informações financeiras, histórico de pagamentos, perfil de crédito e comportamento financeiro, além de interpretar os fatores que mais influenciam as previsões.

### Objetivos específicos
- Realizar uma análise exploratória dos dados;
- Identificar e corrigir problemas de qualidade dos dados;
- Comparar diferentes algoritmos de classificação;
- Otimizar os modelos por meio de ajuste de hiperparâmetros;
- Interpretar as previsões utilizando a técnicas SHAP, de Explainable AI (XAI);
- Discutir possíveis aplicações do modelo em processos de concessão de crédito.

## Etapas da Análise
| **Etapa** | **Descrição** |
| :------- | :------ |
| [Leitura e Exploração Inicial dos Dados](https://github.com/simires/Credit-Score-Classification/blob/main/notebooks/01-leitura_e_exploracao.ipynb) | Etapa inicial onde o conjunto de dados é carregado e explorado para entender as variáveis e problemas que devem ser tratados na limpeza dos dados. |
| [Limpeza e Preparação dos Dados](https://github.com/simires/Credit-Score-Classification/blob/main/notebooks/02-limpeza_e_preparacao.ipynb) | Limpeza das variáveis numéricas e categóricas, onde foram tratados dados ausentes, remoção de caracteres inválidos, correção de valores inconsistentes e de tipos de dados. |
| [Análise Exploratória dos Dados](https://github.com/simires/Credit-Score-Classification/blob/main/notebooks/03-analise_exploratoria.ipynb) | Análises das distribuições dos dados numéricos e categóricos, além da invertigação de suas correlações com a variável alvo da predição. |
| [Modelagem Preditiva](https://github.com/simires/Credit-Score-Classification/blob/main/notebooks/04-modelagem.ipynb) | Treinamento, tuning de hiperparâmetros e avaliação dos modelos de Regressão Logística, Random Forest e LightGBM de acordo com as métricas de Acurácia, Precisão ponderada, Revocação ponderada e F1-score ponderado e macro. Random Forest com os hiperparâmetros padrões foi escolhido como o modelo com melhor desempenho, e a partir disso foram avaliadas suas métricas, predições e explicação do modelo usando SHAP. |
| [Discussão dos Resultados](https://github.com/simires/Credit-Score-Classification/blob/main/notebooks/05-discussao.ipynb) | Nesta etapa são aprensentados os insights adquiridos, recomendações práticas e discussões de perguntas de negócio que não haviam sido respondidas ainda. |

## Escolha dos Modelos
- Três modelos de classificação foram escolhidos para serem avaliados: **Regressão Logística** (para servir de comparação para os outros modelos), **Random Forest**, e **LightGBM**.
- A principal métrica para avaliar o desempenho dos modelos foi o F1-score ponderado, devido os dados possuírem classes desbalanceadas.
- Após a tentativa de tuning dos hiperparãmetros, o modelo que apresentou melhor desempenho foi o Random Forest com hiperparâmetros padrões, que foi escolhido para realizar predições e ter seus resultados explicados.
- Além disso, foi utilizada a técnica SHAP para entender as classificações do modelo e importância das variáveis para as previsões.

## Principais achados e Insights
- Apesar de apresentar um desempenho satisfatório para um problema de classificação multiclasses, classificando corretamente quase 80% da amostra de teste, apenas 71% dos registros que eram Good foram classificados como tal, indicando uma dificuldade do modelo de identificar categorias subrepresentadas.
- As variáveis mais importantes para a classificação do modelo mudam de acordo com a classe que é predita. Para a classe Poor, a variável mais importante é a dívida restante da pessoa, já para Standard e Good é o mix de créditos.

## Recomendações Práticas
- **Para instituições financeiras**, é importante priorizar os indicadores de comportamento financeiro dos clientes (juros, atrasos, dívidas) para a concessão de crédito, e atualizar os scores periodicamente conforme o comportamento das pessoas muda.
- **Para clientes**, as melhores formas de melhorar o score de créditos são: pagar as contas dentro do prazo, diminuir suas dívidas restantes, manter um bom mix de créditos e um histórico financeiro consistente ao longo do tempo
