# Projeto IoT - ESP32, DHT11 e ThingSpeak 🌡️

## Sobre o projeto

Este projeto foi desenvolvido durante meus estudos de IoT.

A ideia foi utilizar um ESP32 para medir temperatura e umidade com o sensor DHT11 e enviar os dados para o ThingSpeak.

## Tecnologias utilizadas

- ESP32
- MicroPython
- DHT11
- ThingSpeak

## O que foi desenvolvido

- Conexão do ESP32 com Wi-Fi
- Leitura de temperatura e umidade
- Controle de um relé
- Envio dos dados para o ThingSpeak
- Monitoramento dos dados

## Funcionamento

O sensor DHT11 realiza a leitura da temperatura e da umidade.

Quando a temperatura passa de 31°C ou a umidade passa de 70%, o relé é acionado.

Os dados são enviados para o ThingSpeak para acompanhamento.

## Objetivo

Praticar programação com MicroPython, utilização de sensores e envio de dados de um dispositivo IoT para uma plataforma online.

## Observação

As informações de Wi-Fi e a API Key do ThingSpeak foram substituídas por valores de exemplo para evitar a exposição de dados pessoais.
