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

### 2. Dados de Entrada

// Dados simulados (substituir por leituras de sensores)
float flowerData[4] = {
    5.1,  // Comprimento sépala (cm)
    3.5,  // Largura sépala (cm)
    1.4,  // Comprimento pétala (cm)
    0.2   // Largura pétala (cm)
};

### 3. Classificação
int classId = classifier.predict(flowerData);
// Saída: 0=Setosa, 1=Versicolor, 2=Virginica

🧠 Dataset Iris (Opcional)
Para testes com amostras limitadas (3 exemplos):
const float irisDataset[3][4] = {
    {5.1, 3.5, 1.4, 0.2},  // Setosa
    {7.0, 3.2, 4.7, 1.4},   // Versicolor
    {6.3, 3.3, 6.0, 2.5}    // Virginica
};
const int irisLabels[3] = {0, 1, 2};

🔄 Fluxo de Trabalho

from sklearn.svm import SVC
from micromlgen import port
model = SVC(kernel='linear').fit(X_train, y_train)
print(port(model))  # Exporta para C++


### ✨ Destaques:
- Usa tabelas para comparações
- Blocos de código com syntax highlighting
- Ícones para melhor visualização (opcional)
- Links para recursos externos

