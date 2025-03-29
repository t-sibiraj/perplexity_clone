import google.generativeai as genai
from config import Settings

settings = Settings()


class LLMService:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.0-flash-exp")

    def generate_response(self, query: str, search_results: list[dict]):

        context_text = "\n\n".join(
            [
                f"Source {i+1} ({result['url']}):\n{result['content']}"
                for i, result in enumerate(search_results)
            ]
        )

        full_prompt = f"""
        Context from web search:
        {context_text}

        Query: {query}

        Please provide a comprehensive, accurate, and well-cited response that directly addresses the query using the context provided above.
        Think carefully and reason through the problem step by step, relying on the given context as much as possible before drawing on external knowledge.
        Only incorporate your own knowledge when it is absolutely necessary and clearly justified.
        Ensure that the final answer is detailed, logically sound, and thoroughly supported by citations or references when appropriate.
        """

        response = self.model.generate_content(full_prompt, stream=True)

        for chunk in response:
            yield chunk.text