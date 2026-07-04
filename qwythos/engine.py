import os
import requests
from llama_cpp import Llama

class QwythosEngine:
    def __init__(self, model_path: str, api_key: str = None, api_endpoint: str = None):
        """
        Initializes the Qwythos AI engine.
        Loads the local GGUF model via llama.cpp or sets up the API fallback.
        """
        self.model_path = model_path
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        
        # Hardware limits configuration (e.g., targeting RTX 3060 12GB VRAM)
        self.max_local_tokens = 8192  # Safe KV-cache limit for local VRAM
        self.llm = None
        
        self._initialize_local_model()

    def _initialize_local_model(self):
        """
        Loads the Qwythos-9B Q4_K_M model into VRAM.
        """
        if os.path.exists(self.model_path):
            # n_gpu_layers=-1 offloads all layers to the GPU
            # n_ctx sets the local context window
            self.llm = Llama(
                model_path=self.model_path,
                n_gpu_layers=-1, 
                n_ctx=self.max_local_tokens,
                verbose=False
            )
            print("Local Qwythos-9B engine initialized successfully.")
        else:
            print("Warning: Model weights not found. Running in API-only mode.")

    def generate_response(self, prompt: str) -> str:
        """
        Hybrid Burst Routing: Determines whether to process locally or via API.
        """
        # Estimate token count (rough estimation: 1 word ~ 1.3 tokens)
        estimated_tokens = int(len(prompt.split()) * 1.3)
        
        if estimated_tokens > self.max_local_tokens and self.api_endpoint:
            print(f"Context too large ({estimated_tokens} tokens). Triggering Hybrid Burst -> API.")
            return self._generate_via_api(prompt)
        else:
            print(f"Processing locally ({estimated_tokens} tokens).")
            return self._generate_locally(prompt)

    def _generate_locally(self, prompt: str) -> str:
        """
        Runs inference entirely on the local GPU.
        """
        if not self.llm:
            return "Error: Local model is not loaded."
            
        output = self.llm(
            prompt,
            max_tokens=2048,
            stop=["User:", "\n\n\n"],
            echo=False
        )
        return output['choices'][0]['text'].strip()

    def _generate_via_api(self, prompt: str) -> str:
        """
        Offloads inference to a user-provided OpenAI-compatible API endpoint.
        """
        if not self.api_key or not self.api_endpoint:
            return "Error: API key/endpoint not configured for Hybrid Burst."
            
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "model": "qwythos-hybrid-backend",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 4096
        }
        
        try:
            response = requests.post(self.api_endpoint, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Hybrid Burst API Error: {str(e)}"
