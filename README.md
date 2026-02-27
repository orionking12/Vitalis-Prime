<div align="center">
  <img src="./Vitalis_Banner.png" alt="Vitalis-Prime v1.0 Logo" width="100%">

  <h1>VITALIS-PRIME: The Convergent Intelligence Kernel (v1.0)</h1>

  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.12-blue.svg" alt="Python 3.12">
  </a>
  <a href="https://pytorch.org/">
    <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?logo=PyTorch&logoColor=white" alt="PyTorch">
  </a>
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/flask-%23000.svg?logo=flask&logoColor=white" alt="Flask">
  </a>
</div>

<br>

**Vitalis-Prime** es un motor de inteligencia neuro-híbrida y un framework de Gemelo Digital Evolutivo. Está diseñado matemáticamente para sobrevivir a colapsos en simulaciones físicas y adaptarse a derivas de concepto (*Concept Drift*) masivas en tiempo real, superando las limitaciones de los ensamblados de Machine Learning estáticos.
---

## 🧠 Arquitectura Central: Sincronizador Neuro-Híbrido

A diferencia de los sistemas tradicionales que promedian predicciones, Vitalis-Prime utiliza un **Módulo de Atención Dinámica** que debate internamente en tiempo real. 

Fusiona la robustez estadística de los árboles de decisión (**Random Forest / Scikit-learn**) con la intuición profunda de extracción de espacios latentes de una red neuronal (**PyTorch**). Optimizada mediante un marco de **Pérdida Dual (Dual Loss)**, la red delega el control al algoritmo clásico en entornos de certidumbre, pero toma el mando de emergencia absoluto cuando el entorno físico cambia sus reglas (Caos Termodinámico/Cuántico).

## 📖 Descripción Extendida: La Filosofía de VITALIS-PRIME

### El Límite de la Inteligencia Artificial Clásica
En entornos de simulación física, computación cuántica o mercados financieros de alta frecuencia, las reglas del entorno no son estáticas. La mayoría de los modelos de *Machine Learning* (como los árboles de decisión o ensamblados tradicionales) sufren de **Deriva de Concepto (Concept Drift)**: memorizan un conjunto de reglas y colapsan catastróficamente cuando el universo físico o el mercado cambian de comportamiento. 

### La Solución: Arbitraje Cognitivo y Resiliencia
**VITALIS-PRIME** no intenta crear un modelo perfecto, sino un ecosistema de modelos que debaten entre sí. Actúa como un árbitro en un estado de "tira y afloja" (*Tug-of-War*) matemático:

1. **La Memoria Rígida (Random Forest):** Proporciona predicciones altamente eficientes y precisas en entornos estables (Normalidad Térmica/Cuántica). Actúa como la base heurística del sistema.
2. **El Espacio Fluido (PyTorch Generator):** Una red profunda que extrae representaciones latentes de los datos. No solo ve números, entiende el contexto y la topología del estado de entrada.
3. **El Árbitro de Confianza (Módulo de Atención Dinámica):** El corazón de Vitalis-Prime. En lugar de hacer un promedio ciego de las decisiones de ambos modelos, la red atencional analiza el estado actual y decide en milisegundos a quién darle el control. Si el entorno se vuelve caótico y el modelo clásico falla, la atención se desplaza violentamente hacia la Red Neuronal para salvar el sistema.

### Innovaciones Matemáticas Clave
* **Dual Loss Framework (Pérdida Dual):** El sistema optimiza sus pesos usando una función de pérdida bifurcada. Obliga al generador neuronal a ser un experto independiente, al mismo tiempo que lo entrena para ser el compañero perfecto del algoritmo clásico.
* **Amnesia Estructurada (Rolling Windows):** Para evitar la ceguera algorítmica, el sistema descarta programáticamente los recuerdos más antiguos. Cuando detecta un cambio en las leyes del entorno, obliga a los modelos clásicos a olvidar su entrenamiento obsoleto y aprender el nuevo paradigma sin detener la ingesta de telemetría.
* **Telemetría Topológica (Holoscopio 3D):** Transforma matrices abstractas de error (*Loss Tensors*) en representaciones físicas tridimensionales. Permite a los operadores humanos "ver" en tiempo real si el sistema está en paz, o si está navegando por un océano de turbulencia cognitiva tratando de adaptarse.

### Casos de Uso Potenciales
* **Industria 4.0 / IoT:** Detección de anomalías térmicas y de vibración en reactores o maquinaria pesada donde las condiciones de operación varían drásticamente.
* **Finanzas Web3 y DeFi:** Análisis predictivo de oráculos y protección contra anomalías en *Smart Contracts* durante periodos de extrema volatilidad.
* **Deep Tech & Simulaciones:** Núcleo de estabilización para arquitecturas de agentes autónomos y motores generativos de alto rendimiento.

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

# 1. Clonar el repositorio
git clone [https://github.com/TU_USUARIO/NOMBRE_REPO.git](https://github.com/TU_USUARIO/NOMBRE_REPO.git)
cd NOMBRE_REPO

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Iniciar el servidor con Gunicorn (4 workers)
./run_prod.sh

🔬 Modo de Uso (Prueba de Estrés)
Para observar el ecosistema completo operando bajo estrés extremo, ejecuta en tres terminales independientes:

Inicia el Núcleo (API): python servidor_nucleo.py

Inicia el Holoscopio: python holoscopio_visual.py (Abre http://127.0.0.1:8050)

Lanza el Enjambre: python enjambre_adversario.py

Observa el navegador: En la ronda 7, el Enjambre invertirá las leyes físicas. Verás el océano de pérdida agitarse y a la Red Neuronal arrancar la atención gravitacional del Random Forest para salvar el sistema.

👤 Autor y Contacto Comercial
Jorge Humberto Davalos Gonzalez Arquitecto Tecnológico y Creador

Email: luckystrike@gmail.com

Ubicación: Tlaquepaque / Guadalajara, Jalisco, México.

Para consultas sobre licencias comerciales, escalabilidad en entornos de Industria 4.0, implementaciones empresariales, integración Web3 o colaboraciones directas relacionadas con el núcleo VITALIS-PRIME o cualquier arquitectura derivada, por favor contactar directamente a través del correo electrónico proporcionado.

Licencia: Distribuido bajo licencia MIT. Ver archivo LICENSE para más detalles.
