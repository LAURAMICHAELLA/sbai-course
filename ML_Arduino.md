# microML para Arduino: Classificação do Dataset Iris

Este projeto demonstra como implementar um classificador SVM para o dataset Iris usando a biblioteca `microML` no Arduino.

microML é uma implementação simplificada de machine learning para microcontroladores como Arduino, permitindo que você execute modelos de aprendizado de máquina diretamente em dispositivos embarcados.

## Como utilizar microML no Arduino

# Pré-requisitos:
Instale a biblioteca microML no Arduino IDE:

Vá em "Sketch" > "Incluir Biblioteca" > "Gerenciar Bibliotecas"

Busque por "microml" e instale a biblioteca

# Prepare seu modelo de machine learning (geralmente criado em Python com scikit-learn) e converta-o para formato compatível com Arduino.

-- Passos básicos:
-Treine seu modelo em Python
-Use o gerador de código do microML para exportar o modelo
-Copie o código gerado para seu sketch Arduino
- Implemente a lógica de coleta de dados e predição

## ⚠️ Atenção
- O Arduino **não carrega o dataset completo** devido a limitações de memória.
- O modelo é **pré-treinado em Python** e exportado para C++.
- Novos dados são classificados em tempo real (via sensores ou arrays fixos).

### Código completo
```cpp
#include <microml.h>

// 1. MODELO PRÉ-TREINADO (exportado do Python)
const float supportVectors[] = { /* ... */ };  // Vetores do SVM
const float coefficients[] = { /* ... */ };    // Coeficientes do modelo
const float intercept = -0.0588;               // Viés (bias)
SVMClassifier classifier(/* ... */);           // Classificador

void setup() {
    Serial.begin(9600);
}

void loop() {
    // 2. DADOS DE ENTRADA (substitua isso pelos seus dados reais)
    float flowerData[4] = {
        5.1,  // Comprimento da sépala (cm)
        3.5,   // Largura da sépala (cm)
        1.4,   // Comprimento da pétala (cm)
        0.2    // Largura da pétala (cm)
    };

    // 3. CLASSIFICAÇÃO (o modelo usa os dados acima)
    int classId = classifier.predict(flowerData);

    // Exemplo de saída:
    Serial.print("Classe: ");
    Serial.println(classId);  // 0=Setosa, 1=Versicolor, 2=Virginica
    delay(1000);
}
```
## 📋 Explicação do Código Arduino

### 1. Modelo Pré-treinado (C++)
```cpp
// Modelo SVM exportado do Python
const float supportVectors[] = { /* ... */ };  // Vetores de suporte
const float coefficients[] = { /* ... */ };    // Coeficientes do modelo
const float intercept = -0.0588;               // Viés (bias)
SVMClassifier classifier(/* ... */);           // Instância do classificador
```
### 2. Dados de Entrada

```cpp
// Dados simulados (substituir por leituras de sensores)
float flowerData[4] = {
    5.1,  // Comprimento sépala (cm)
    3.5,  // Largura sépala (cm)
    1.4,  // Comprimento pétala (cm)
    0.2   // Largura pétala (cm)
};
```

### 3. Classificação

```cpp
// 3. CLASSIFICAÇÃO (o modelo usa os dados acima)
    int classId = classifier.predict(flowerData);

    // Exemplo de saída:
    Serial.print("Classe: ");
    Serial.println(classId);  // 0=Setosa, 1=Versicolor, 2=Virginica
```

### 4. 🧠 Alteração no código para teste com amostras Dataset Iris (Opcional)
Para testes com amostras limitadas (3 exemplos):

```cpp
// Dataset Iris reduzido (exemplo com 3 amostras)
const float irisDataset[3][4] = {
    {5.1, 3.5, 1.4, 0.2},  // Setosa
    {7.0, 3.2, 4.7, 1.4},   // Versicolor
    {6.3, 3.3, 6.0, 2.5}    // Virginica
};
const int irisLabels[3] = {0, 1, 2};  // Labels correspondentes

void loop() {
    // Classifica cada amostra
    for (int i = 0; i < 3; i++) {
        int prediction = classifier.predict(irisDataset[i]);
        Serial.print("Amostra ");
        Serial.print(i);
        Serial.print(": ");
        Serial.println(prediction == irisLabels[i] ? "Correto" : "Erro");
    }
    delay(5000);
}
```
Observação: provavelmente você não conseguirá carregar o dataset completo devido a limitação de memória: O Arduino Uno (por exemplo) tem apenas 2KB de RAM.
O dataset Iris completo (150 amostras × 4 features) não caberia.

### 5. 🔄 Fluxo de Trabalho
# Treinar a base em python utilizando qualquer IDE que compile o arquivo `.py`:

```python
from sklearn.svm import SVC
from micromlgen import port
from sklearn.datasets import load_iris

# Carrega o dataset Iris
X, y = load_iris(return_X_y=True)

# Treina o modelo
model = SVC(kernel='linear').fit(X, y)

# Gera o código C++ para o Arduino
print(port(model))  # Copie a saída para substituir no código Arduino
```
```
# Observação:
O dataset é carregado apenas durante o treinamento.
O Arduino só recebe o modelo já treinado (não o dataset completo).

### 6. Implementar no Arduino
```cpp
#include <microml.h>
#include <Arduino.h>

// 1. Modelo SVM pré-treinado (exportado do Python)
const float supportVectors[] = { /* ... */ };  // Vetores de suporte
const float coefficients[] = { /* ... */ };    // Coeficientes
const float intercept = -0.0588;               // Bias
const int nClasses = 3;
const int nSupports = 3;
const int nFeatures = 4;

SVMClassifier classifier(
    supportVectors,
    coefficients,
    intercept,
    nClasses,
    nSupports,
    nFeatures
);

void setup() {
    Serial.begin(9600);
    while (!Serial);
    Serial.println("Classificador Iris com microML");
}

void loop() {
    // 2. Dados de entrada (simulados ou de sensores)
    float input[4] = {5.1, 3.5, 1.4, 0.2};  // Exemplo: Iris Setosa
    
    // 3. Classificação
    int prediction = classifier.predict(input);
    
    // 4. Saída
    Serial.print("Classe prevista: ");
    switch(prediction) {
        case 0: Serial.println("Iris Setosa"); break;
        case 1: Serial.println("Iris Versicolor"); break;
        case 2: Serial.println("Iris Virginica"); break;
    }
    delay(2000);
}
```
### 6. O que você precisa fazer:

Substituir os placeholders (/* ... */) pelos valores reais do seu modelo exportado do Python (usando micromlgen).

Adaptar os dados de entrada:

Pode ser um array fixo (como no exemplo) ou Dados lidos de sensores '(ex: float input[4] = {sensor1.read(), sensor2.read(), ...};)'.



### 📌 Limitações
Item	                    Detalhe
Memória RAM	                Apenas ~2KB no Arduino Uno
Tamanho do Dataset	        Máximo 10-20 amostras (tipicamente)
Complexidade	            Modelos lineares funcionam melhor

# 🔗 Recursos Úteis

- [Biblioteca microML](https://github.com/eloquentarduino/micromlgen)
- [Dataset Iris](https://www.tinyml.org/](https://archive.ics.uci.edu/dataset/53/iris)






