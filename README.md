# Perpexility Clone


A streamlined Perplexity-style AI search assistant built with **Flutter** and **FastAPI**, powered by modern LLMs and real-time streaming chat.


https://github.com/user-attachments/assets/ab49652c-3107-4a7a-8f7c-a3b01296d954

## ✨ Features

- 🔍 Ask questions, get AI-generated answers with real-time citations.
- 📡 WebSocket-based live streaming responses.
- 📱 Mobile-optimized UI with loading skeletons.
- 📝 Rich markdown rendering for answers.
- 🤖 Connects to external knowledge sources for dynamic, grounded responses.

## 🧠 How It Works

1. **Frontend**: Built in Flutter, it provides a smooth chat interface with markdown support and loading states.
2. **Backend**: FastAPI powers a chat endpoint with real-time WebSocket support.
3. **AI Integration**: Uses Gemini (or other LLMs) to generate answers based on online search results.
4. **Search & Relevance**: 
   - Documents are fetched from online sources using tools like **Trafilatura** and **Tavily**.
   - They are ranked using **cosine similarity** (a mathematical technique to measure how similar two pieces of text are).
   - The most relevant snippets are passed into the prompt for the LLM to generate a contextual response.

### 🧮 What is Cosine Similarity?

Cosine similarity is a way to compare two texts by measuring the **angle between their vector representations**. A smaller angle (closer to 1) means the texts are more similar. This is useful for picking the most relevant search results to feed into the LLM.

## 📦 Dependencies

### Flutter (Frontend)
```yaml
dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.8
  web_socket_client: ^0.2.0
  google_fonts: ^6.2.1
  flutter_markdown: ^0.7.6+2
  skeletonizer: ^1.4.3
```


### Python (Backend)
| Package | Purpose |
|--------|---------|
| `fastapi` | Lightweight, high-performance web framework for serving the chat API and WebSocket endpoints. |
| `google-ai-generativelanguage` | Client library to interact with Google’s Gemini LLMs. |
| `huggingface-hub` | Fetches and manages embeddings/models from Hugging Face's model repository. |
| `tavily-python` | Programmatic search API to find relevant documents and web sources in real-time. |
| `trafilatura` | Extracts clean text content from raw HTML pages, removing ads, navigation, etc. |
| `transformers` | Used for text embeddings and model inference (e.g., to compute cosine similarity). |
