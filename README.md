# Telemetria SMC - Simulador de Smart Grids

Este repositório contém um módulo em Python desenvolvido para simular o fluxo de telemetria em **Sistemas de Medição Centralizada (SMC)** de smart grids. O foco principal do projeto é demonstrar a aplicação prática de conceitos avançados de programação voltados para a eficiência de infraestrutura de dados no setor elétrico.

## Tecnologias e Conceitos Utilizados

* **Python 3**
* **Programação Orientada a Objetos (POO):** Estruturação de classes para modelagem de componentes do setor elétrico.
* **Geradores (Generators - `yield`):** Implementação de *lazy evaluation* para processamento de grandes volumes de dados (Big Data), garantindo o consumo mínimo de memória RAM ao tratar leituras de medidores uma a uma.

## Contexto Técnico

No cenário moderno de distribuição de energia, a coleta contínua de dados de consumo ativo (kWh) exige arquiteturas de software otimizadas. Este algoritmo simula o recebimento de telemetria em tempo real para medições de baixa tensão, classificando as demandas de pico flutuante e operações normais de forma dinâmica e escalável.
