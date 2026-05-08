# Análise e Processamento de Débitos Municipais

Projeto desenvolvido em Python para filtragem e exportação parametrizada de registros de débitos municipais fictícios da cidade de Vitória/ES realizado para o processo seletivo do LabCidades.

A parte do tratamento dos dados é explicada no notebook contido em /notebooks.

O sistema em si presente em /src realiza leitura da base tratada, validação de parâmetros e exportação de subconjuntos da base conforme a situação de pagamento e variáveis selecionadas.

---

#  Bibliotecas Utilizadas

- Pandas: Manipulação de Dados
- Unicode: Normalização textual

---

# Lógica Geral do Processamento

O processamento foi dividido nas seguintes etapas:

## 1. Leitura da base tratada
A base `debitos_tratados.csv` é carregada utilizando Pandas.

---

## 2. Leitura do arquivo de parâmetros
O sistema realiza leitura do arquivo `parametros.txt`, responsável por definir:
- situação de pagamento;
- variáveis desejadas na saída.

---

## 3. Validação do arquivo de parâmetros
São realizadas verificações de:
- estrutura do arquivo;
- situação de pagamento válida;
- existência das variáveis solicitadas.

---

## 4. Filtragem dos registros
Os registros são filtrados conforme a situação de pagamento definida.

---

## 5. Exportação da saída
O subconjunto filtrado é exportado para:

```text
data/processed/saida.csv
```

---

# Reprodução do Projeto

## 1. Clone o repositório

```bash
git clone https://github.com/vss10/Processo-LabCidades.git
```

---

## 2. Entre na pasta do projeto

```bash
cd projeto-dividas-municipais
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Verifique a estrutura dos arquivos

Os arquivos devem estar organizados da seguinte forma:

```text
data/processed/debitos_tratados.csv
parametros/parametros.txt
```

---

## 5. Execute o programa

Na raiz do projeto:

```bash
python src/main.py
```

--- 

# Resultado

O arquivo gerado será salvo em:

```text
data/processed/saida.csv
```

---

# Tratamento de Erros

O programa realiza validações para:

- arquivos inexistentes;
- erros de leitura;
- arquivo de parâmetros inválido;
- situação de pagamento inválida;
- variáveis inexistentes;
- erros de exportação.

---
