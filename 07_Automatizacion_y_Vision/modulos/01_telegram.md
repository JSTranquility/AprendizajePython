# 🤖 Especialización en Bots de Telegram

Python es excelente para crear bots de Telegram. Generalmente se usa la librería `python-telegram-bot` o `aiogram`.

## 🎯 Conceptos Clave
1. **BotFather**: Cómo obtener tu Token de API oficial.
2. **Handlers**: Funciones que responden a comandos (`/start`) o mensajes de texto.
3. **Dispatcher / Router**: La lógica que decide qué handler debe procesar cada mensaje.
4. **Context y Data**: Cómo guardar el estado de una conversación con un usuario.
5. **Teclados (Keyboards)**: InlineKeyboards (botones en el chat) y ReplyKeyboards (botones en el teclado).

## 🚀 Tu Primer Desafío
Crea un bot que:
- Al recibir el comando `/start`, salude al usuario por su nombre.
- Al recibir el comando `/clima`, le pida al usuario su ciudad y le devuelva un texto (puedes inventar el clima por ahora).
- Use botones (Inline Buttons) para que el usuario elija entre dos opciones.

## 📚 Recursos
- [Documentación oficial de python-telegram-bot](https://python-telegram-bot.org/)
- [Telegram Bot API (Oficial)](https://core.telegram.org/bots/api)
