# Análise e Modelagem de Dados de Fraude em Cartão de Crédito

Este projeto utiliza dados de transações de cartão de crédito para detectar fraudes. O objetivo é construir um modelo de regressão logística para classificar transações como fraudulentas ou não fraudulentas. O código inclui a preparação dos dados, treinamento do modelo e validação.

## Estrutura do Projeto

1. **Importação de Bibliotecas**
   - `pandas`: Manipulação e análise de dados.
   - `numpy`: Operações numéricas.
   - `zipfile`: Manipulação de arquivos ZIP.
   - `sklearn`: Modelagem e avaliação de modelos de machine learning.

2. **Carregamento dos Dados**
   - Os dados são carregados de um arquivo ZIP contendo um CSV com informações de transações de cartão de crédito.

3. **Preparação dos Dados**
   - Verificação de valores nulos e tipos de dados.
   - Separação dos dados em transações fraudulentas e não fraudulentas.
   - Balanceamento do dataset para igualar o número de transações fraudulentas e não fraudulentas.

4. **Validação dos Dados**
   - Extração e validação de amostras para verificação posterior.
   - Remoção das amostras de validação do conjunto de treinamento.

5. **Treinamento do Modelo**
   - Divisão dos dados em conjuntos de treinamento e teste.
   - Treinamento de um modelo de regressão logística.
   - Avaliação do modelo utilizando acurácia.

6. **Validação Final**
   - Predição das transações de validação e comparação com os valores reais.

## Passos para Executar

1. **Instalar Dependências**
   Certifique-se de que as seguintes bibliotecas estão instaladas:
   ```bash
   pip install pandas numpy scikit-learn

2. **Preparar os Dados**
   - Coloque o arquivo ZIP contendo o CSV dos dados de cartão de crédito
   - 'C:\\data\\creditcard.zip.'

3. **Executar o código**
   - Execute o script Python para carregar os dados, treinar o modelo e gerar previsões.
  
## Resultados
   - Acurácia do modelo: (substitua este texto pela acurácia obtida após a execução do código)
   - Comparação entre valores reais e previsões para amostras de validação.
 
## Contribuição
   Se você deseja contribuir para este projeto, sinta-se à vontade para enviar pull requests ou abrir issues para discutir melhorias.
