---
name: conferir-visual
description: Tira screenshots da landing page do Sessão.Café (index.html) em largura de celular (375px) e de desktop e mostra a primeira dobra de cada uma. Use sempre logo depois de qualquer alteração visual na landing page — mudanças em style.css, no HTML/markup do index.html, cores, tipografia, espaçamento, layout, imagens, ícones do sprite ou favicon — e também quando o usuário pedir para "ver como ficou", "conferir no celular" ou "tirar print da página". Não use para mudanças só em texto de FAQ sem efeito de layout, nem para alterações que não tocam a página.
---

# Conferir visual (mobile 375px + desktop)

Depois de uma alteração visual na landing page, mostre ao usuário como ficou a
**primeira dobra** (o que aparece sem rolar) no celular e no desktop.

## Passos

1. **Subir a página no navegador embutido** (ferramentas `mcp__Claude_Browser__*`).
   - `preview_start` com `name: "landing"` (definido em `.claude/launch.json`: roda
     `.claude/servir_landing.py` na porta 8123, que só entrega arquivos da página e
     bloqueia `.env` e afins). Ele reaproveita o servidor se já estiver rodando. Anote o `tabId` que ele devolve e use em todos os passos.
   - Não abra o `index.html` via `file://`: o navegador embutido transforma em
     snapshot e o `style.css` não carrega.

2. **Celular — 375px.**
   - `resize_window` com `width: 375`, `height: 812` (a altura é a primeira dobra).
   - `navigate` para `http://localhost:8123/` (recarrega e pega o CSS novo).
   - `computer` → `wait` de 2 segundos: o hero tem animação de entrada e o print
     sai esbranquiçado se for tirado antes.
   - `javascript_tool`: `window.scrollTo(0, 0); document.documentElement.scrollWidth > window.innerWidth`
     — se der `true`, há rolagem horizontal; avise e tente achar o elemento que vaza.
   - `computer` → `screenshot`. Esse é o print da primeira dobra no celular.

3. **Desktop.**
   - `resize_window` com `width: 1280`, `height: 800`.
   - `navigate` para a mesma URL, `wait` de 2 segundos, `window.scrollTo(0, 0)`,
     `screenshot`.

4. **Restaurar a janela:** `resize_window` com `preset: "desktop"` ao terminar.
   Dá para fazer os passos 2–4 de uma vez com `browser_batch`.

5. **Responder ao usuário** com os dois prints (celular primeiro, depois desktop) e,
   em 2–4 linhas, o que chamou atenção: algo cortado, texto quebrando feio, botão
   escondido abaixo da dobra, contraste ruim, rolagem horizontal. Se estiver tudo
   certo, diga isso em uma linha — não invente problema.

## Observações

- Não altere código durante esta conferência. Se achar um problema, aponte e pergunte
  se deve corrigir.
- Se o servidor não subir (porta ocupada, Python ausente), veja `preview_logs` e avise
  o usuário em vez de trocar para o Chrome dele sem perguntar.
