# 🌌 VITALIS-PRIME: The Convergent Intelligence Kernel (v1.0)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

**Vitalis-Prime** es un motor de inteligencia neuro-híbrida y un framework de Gemelo Digital Evolutivo. Está diseñado matemáticamente para sobrevivir a colapsos en simulaciones físicas y adaptarse a derivas de concepto (*Concept Drift*) masivas en tiempo real, superando las limitaciones de los ensamblados de Machine Learning estáticos.

---

## 🧠 Arquitectura Central: Sincronizador Neuro-Híbrido

A diferencia de los sistemas tradicionales que promedian predicciones, Vitalis-Prime utiliza un **Módulo de Atención Dinámica** que debate internamente en tiempo real. 

Fusiona la robustez estadística de los árboles de decisión (**Random Forest / Scikit-learn**) con la intuición profunda de extracción de espacios latentes de una red neuronal (**PyTorch**). Optimizada mediante un marco de **Pérdida Dual (Dual Loss)**, la red delega el control al algoritmo clásico en entornos de certidumbre, pero toma el mando de emergencia absoluto cuando el entorno físico cambia sus reglas (Caos Termodinámico/Cuántico).

## 🚀 Ecosistema de Componentes

El repositorio se divide en tres microservicios concurrentes:

1. **El Cerebro (`servidor_nucleo.py`)**: 
   Servidor asíncrono en Flask que ingiere telemetría mediante micro-batching. Aplica *Amnesia Estructurada* (ventanas móviles) para reentrenar sus modelos clásicos sin detener la ingesta de datos.
2. **Los Ojos (`holoscopio_visual.py`)**: 
   Un Holoscopio de Resonancia Cognitiva construido en Dash/Plotly 3D. No grafica simples líneas; renderiza la tensión atencional entre los modelos como fuerzas gravitacionales y visualiza el error del sistema como un "Océano de Pérdida" topográfico.
3. **El Sistema Nervioso (`enjambre_adversario.py`)**: 
   Un cliente de pruebas de estrés asíncrono (*Adversarial Swarm*) que inyecta ruido y altera deliberadamente las "leyes de la física" de la simulación para probar la antifragilidad del núcleo.

---

## 🛠️ Instalación y Despliegue

### Opción 1: Despliegue en la Nube (Docker)
El proyecto incluye un `Dockerfile` multi-stage optimizado para plataformas como Render, Railway o AWS.
```bash
docker build -t vitalis-prime:v1.0 .
docker run -p 5000:5000 -p 8050:8050 vitalis-prime:v1.0
