# Qwythos Deployment on Kali Linux

This guide provides multiple methods to deploy Qwythos on Kali Linux, from CLI-only to full GUI support.

## System Requirements

- **Kali Linux** (2024.x recommended)
- **GPU Support**: NVIDIA RTX 3060 12GB+ VRAM (with CUDA)
- **Storage**: 10GB for model weights (Q4_K_M quantization)
- **RAM**: 8GB minimum
- **Python**: 3.10+

## Method 1: CLI Headless Deployment (Fastest, Recommended for Kali)

Ideal for security research and red teaming operations without GUI overhead.

### Prerequisites

```bash
sudo apt update
sudo apt install -y python3.10 python3.10-venv python3-pip git
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev

# CUDA support (optional but recommended for RTX 3060)
sudo apt install -y nvidia-cuda-toolkit nvidia-driver-535

# Verify CUDA
nvidia-smi
```

### Installation

```bash
# Clone the repository
git clone https://github.com/grottschecq-beep/qwythos.git
cd qwythos

# Create virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt llama-cpp-python[cuda]

# Download the model (5.6GB)
mkdir -p models
cd models
wget https://huggingface.co/empero-ai/Qwythos-9B-Q4_K_M/resolve/main/model.gguf
cd ..
```

### Usage - CLI Interface

```bash
source venv/bin/activate
python3 << 'EOF'
from qwythos.engine import QwythosEngine

# Initialize the engine
engine = QwythosEngine(
    model_path="models/model.gguf",
    api_key=None,  # Optional: Add API fallback
    api_endpoint=None
)

# Test query
response = engine.generate_response("Explain SQL injection to a pentester")
print(response)
EOF
```

### Create Python Wrapper Script

Save as `run_qwythos.py`:

```python
#!/usr/bin/env python3
import sys
import os
from qwythos.engine import QwythosEngine
from qwythos.sandbox import LocalSandbox

def main():
    model_path = "models/model.gguf"
    workspace_dir = os.getcwd()
    
    # Initialize engine
    engine = QwythosEngine(model_path=model_path)
    sandbox = LocalSandbox(workspace_dir=workspace_dir)
    
    print("🔍 Qwythos CLI Interface")
    print("=" * 50)
    print("Type 'exit' to quit\n")
    
    while True:
        try:
            prompt = input("You: ").strip()
            
            if prompt.lower() in ['exit', 'quit']:
                print("Exiting Qwythos.")
                break
            
            if not prompt:
                continue
            
            print("\n⚙️  Processing...\n")
            response = engine.generate_response(prompt)
            
            # Execute any tool calls
            final_response = sandbox.parse_and_execute(response)
            
            print(f"Qwythos: {final_response}\n")
            
        except KeyboardInterrupt:
            print("\n\nInterrupted. Exiting.")
            break
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
```

Make it executable:
```bash
chmod +x run_qwythos.py
./run_qythos.py
```

---

## Method 2: GUI Deployment (With CustomTkinter)

For users who need a graphical interface on Kali.

### Install GUI Dependencies

```bash
# X11 libraries for GUI on Linux
sudo apt install -y python3-tk python3-dev libx11-dev libgl1-mesa-glx

# Install GUI package
source venv/bin/activate
pip install customtkinter>=5.2.2
```

### Create GUI Wrapper Script

Save as `qwythos_gui.py`:

```python
#!/usr/bin/env python3
import customtkinter as ctk
import threading
from qwythos.engine import QwythosEngine
from qwythos.sandbox import LocalSandbox

class QwythosGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Qwythos - Uncensored LLM")
        self.root.geometry("900x700")
        
        self.engine = QwythosEngine(model_path="models/model.gguf")
        self.sandbox = LocalSandbox(workspace_dir=".")
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header = ctk.CTkLabel(
            self.root,
            text="Qwythos 9B - Kali Linux Edition",
            font=("Arial", 18, "bold")
        )
        header.pack(pady=10)
        
        # Chat display
        self.chat_display = ctk.CTkTextbox(
            self.root,
            width=800,
            height=400,
            state="disabled"
        )
        self.chat_display.pack(padx=10, pady=10)
        
        # Input frame
        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(padx=10, pady=10, fill="both", expand=False)
        
        self.input_field = ctk.CTkEntry(input_frame, placeholder_text="Ask Qwythos...")
        self.input_field.pack(side="left", fill="both", expand=True, padx=5)
        self.input_field.bind("<Return>", lambda e: self.send_message())
        
        send_btn = ctk.CTkButton(
            input_frame,
            text="Send",
            command=self.send_message,
            width=100
        )
        send_btn.pack(side="right", padx=5)
    
    def send_message(self):
        prompt = self.input_field.get().strip()
        if not prompt:
            return
        
        self.input_field.delete(0, "end")
        self.append_to_chat(f"You: {prompt}\n")
        
        # Run in thread to prevent UI freeze
        threading.Thread(target=self.get_response, args=(prompt,)).start()
    
    def get_response(self, prompt):
        try:
            response = self.engine.generate_response(prompt)
            final_response = self.sandbox.parse_and_execute(response)
            self.append_to_chat(f"Qwythos: {final_response}\n\n")
        except Exception as e:
            self.append_to_chat(f"Error: {e}\n\n")
    
    def append_to_chat(self, text):
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", text)
        self.chat_display.see("end")
        self.chat_display.configure(state="disabled")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    root = ctk.CTk()
    app = QwythosGUI(root)
    root.mainloop()
```

Run it:
```bash
chmod +x qwythos_gui.py
./qwythos_gui.py
```

---

## Method 3: Docker Deployment (Most Isolated)

For containerized, reproducible deployments.

### Dockerfile

Create `Dockerfile.linux`:

```dockerfile
FROM nvidia/cuda:12.1-runtime-ubuntu22.04

# Install Python and dependencies
RUN apt update && apt install -y \
    python3.10 \
    python3-pip \
    git \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    wget

WORKDIR /app

# Clone repo and install Python deps
RUN git clone https://github.com/grottschecq-beep/qwythos.git .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install llama-cpp-python[cuda]

# Download model
RUN mkdir -p models && \
    cd models && \
    wget https://huggingface.co/empero-ai/Qwythos-9B-Q4_K_M/resolve/main/model.gguf && \
    cd ..

# Copy CLI wrapper
COPY run_qwythos.py .

# GPU passthrough
ENV NVIDIA_VISIBLE_DEVICES=all

ENTRYPOINT ["python3", "run_qwythos.py"]
```

### Build & Run

```bash
# Build the image
docker build -f Dockerfile.linux -t qwythos-kali:latest .

# Run with GPU support
docker run --gpus all -it \
  -v $(pwd)/workspace:/app/workspace \
  qwythos-kali:latest
```

---

## Method 4: WSL2 Deployment (Windows → Kali)

If running Kali in WSL2 on Windows with a physical NVIDIA GPU:

```bash
# Inside WSL2 Kali environment
wsl --list --verbose  # Verify WSL2

# Install NVIDIA CUDA for WSL
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get install cuda-toolkit-12-1

# Then follow Method 1 (CLI)
```

---

## Performance Tuning for Kali Linux

### Optimize for RTX 3060

Add to engine initialization:

```python
from llama_cpp import Llama

llm = Llama(
    model_path="models/model.gguf",
    n_gpu_layers=-1,           # All layers on GPU
    n_ctx=8192,                # Local context (8K for RTX 3060)
    n_threads=8,               # Adjust to your CPU core count
    f16_kv=True,              # Use float16 for KV cache
    verbose=False
)
```

### Disable System Telemetry (Zero-Trust)

```bash
# Disable any collection services
sudo systemctl disable apport
sudo systemctl disable whoopsie
sudo ufw disable  # Optional: If using firewall restrictions
```

### Monitor GPU Usage

```bash
# Terminal 1: Run Qwythos
./run_qwythos.py

# Terminal 2: Monitor GPU
watch -n 1 nvidia-smi
```

---

## Troubleshooting

### 1. CUDA Not Detected

```bash
# Verify CUDA installation
nvcc --version
nvidia-smi

# If missing, install CUDA:
sudo apt install nvidia-cuda-toolkit
```

### 2. Model Download Failures

```bash
# Manual download
cd models
wget https://huggingface.co/empero-ai/Qwythos-9B-Q4_K_M/resolve/main/model.gguf
# Or use curl with resume
curl -C - -o model.gguf https://huggingface.co/empero-ai/Qwythos-9B-Q4_K_M/resolve/main/model.gguf
```

### 3. Out of Memory

```python
# Reduce context window in engine.py
self.max_local_tokens = 4096  # Instead of 8192
```

### 4. CustomTkinter GUI Issues (Headless Kali)

Use X11 forwarding:
```bash
# On remote machine
ssh -X kali-user@kali-box
python3 qwythos_gui.py
```

---

## Security Considerations for Red Teaming

1. **Air-Gapped Operation**: Run in isolated network environment
2. **Sandboxing**: Use the included `LocalSandbox` class for tool execution
3. **No Data Retention**: All queries stay local; never transmitted
4. **File Access Restrictions**: Sandbox restricts execution to workspace directory

---

## Next Steps

- **Customize Prompts**: Edit system prompts for specific infosec domains
- **Integrate with Metasploit**: Call Qwythos from Ruby/Python MSF modules
- **Red Team Workflows**: Chain with `hashcat`, `sqlmap`, `nmap` via tool_call
- **Model Fine-tuning**: Distill Qwythos for specific pentesting tasks

---

## References

- [llama.cpp Documentation](https://github.com/ggerganov/llama.cpp)
- [CustomTkinter Docs](https://customtkinter.tomschimansky.com/)
- [NVIDIA CUDA for Kali](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
