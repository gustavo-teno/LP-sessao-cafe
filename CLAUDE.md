# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é

Protótipo para o **Sessão.Café**, uma cafeteria fictícia em João Pessoa para universitários e quem trabalha remoto.

Instrução - ícones: adicione ícones novos ao sprite em vez de colar SVGs soltos.

## Comportamento em JavaScript (fim do arquivo)

JS puro no estilo ES5 (`var`, `function`), sem bibliotecas. Mantenha esse estilo.

- **Modal das ações fictícias:** como é um protótipo, os botões de WhatsApp, Instagram, cupom e cardápio não levam a lugar nenhum. 
HTML inserido depois precisa chamar `bindModals(root)`, como faz `showSpot`. O endereço e os contatos são fictícios de propósito.
