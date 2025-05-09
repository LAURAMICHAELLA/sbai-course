# microML para Arduino: Classificação do Dataset Iris

Este projeto demonstra como implementar um classificador SVM para o dataset Iris usando a biblioteca `microML` no Arduino.

## ⚠️ Atenção
- O Arduino **não carrega o dataset completo** devido a limitações de memória.
- O modelo é **pré-treinado em Python** e exportado para C++.
- Novos dados são classificados em tempo real (via sensores ou arrays fixos).

## 📋 Estrutura do Código

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
int classId = classifier.predict(flowerData);
// Saída: 0=Setosa, 1=Versicolor, 2=Virginica
```

### 4. 🧠 Dataset Iris (Opcional)
Para testes com amostras limitadas (3 exemplos):

```cpp
const float irisDataset[3][4] = {
    {5.1, 3.5, 1.4, 0.2},  // Setosa
    {7.0, 3.2, 4.7, 1.4},   // Versicolor
    {6.3, 3.3, 6.0, 2.5}    // Virginica
};
const int irisLabels[3] = {0, 1, 2};
```

### 5. 🔄 Fluxo de Trabalho
Treinar em Python:

```python
from sklearn.svm import SVC
from micromlgen import port
model = SVC(kernel='linear').fit(X_train, y_train)
print(port(model))  # Exporta para C++
```


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

### 7. Como gerar o modelo em Python (para obter os valores exatos):
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

### 📌 Limitações
Item	                    Detalhe
Memória RAM	                Apenas ~2KB no Arduino Uno
Tamanho do Dataset	        Máximo 10-20 amostras (tipicamente)
Complexidade	            Modelos lineares funcionam melhor

###  🔗 Recursos Úteis
Biblioteca microML

Dataset Iris

Exemplos completos


### ✨ Destaques:
- Usa tabelas para comparações
- Blocos de código com syntax highlighting
- Ícones para melhor visualização (opcional)
- Links para recursos externos

Você pode copiar este Markdown diretamente para um arquivo `README.md` no seu repositório GitHub!

