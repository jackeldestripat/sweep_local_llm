from langchain_community.llms import Ollama
from loguru import logger

from sweepai.config.server import BASERUN_API_KEY
from sweepai.logn.cache import file_cache

if BASERUN_API_KEY is not None:
    pass

OPENAI_TIMEOUT = 60  # one minute

OPENAI_EXCLUSIVE_MODELS = [
    "gpt-4-1106-preview",
    "gpt-3.5-turbo-1106",
    "gpt-3.5-turbo-1106",
]
SEED = 100
logger.info(f"LOADING MIXTRAL HARDCODED")
from langchain_community.llms import Ollama


class OpenAIProxy:
    @file_cache(ignore_params=[])
    def call_openai(self, model, messages, max_tokens, temperature) -> str:
        logger.info(f"MESSAGES:{messages}")
        prompt = "\n".join(
            msg["content"] for msg in messages if msg["role"] in ["user", "assistant"]
        )

        ollama = Ollama(model="dolphin-mixtral")

        response = ollama.invoke(prompt)
        logger.info(f"******************R:{response}")
        return response

    def determine_openai_engine(self, model):
        engine = "Ollama"
        return engine

    def create_openai_chat_completion(
        self, engine, base_url, api_key, model, messages, max_tokens, temperature
    ):
        logger.info(f"MESSAGES:{messages}")
        ollama = Ollama(model="dolphin-mixtral")
        prompt = "\n".join(
            msg["content"] for msg in messages if msg["role"] in ["user", "assistant"]
        )
        response = ollama.invoke(prompt)
        logger.info(f"******************R:{response}")
        return response

    def set_openai_default_api_parameters(
        self, model, messages, max_tokens, temperature
    ):
        logger.info(f"MESSAGES:{messages}")
        ollama = Ollama(model="dolphin-mixtral")
        prompt = "\n".join(
            msg["content"] for msg in messages if msg["role"] in ["user", "assistant"]
        )
        response = ollama.invoke(prompt)
        logger.info(f"******************R:{response}")
        return response
