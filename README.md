
```mermaid
graph LR
    subgraph Ingestion
    A[Supply Chain Data] --> SC[Procurement Logic]
    B[Energy Audit Data] --> EN[Energy Logic]
    end

    subgraph Intelligence_Kernel
    SC -->|Flag High-Cost Asset| MEM[(System Memory JSON)]
    EN -->|Cross-Reference| MEM
    MEM -->|Contextual Analysis| LLM{Llama 3.2 Local}
    end

    subgraph Reporting_Layer
    LLM -->|Generate Decision| LOG[Neural_Log.txt]
    LOG -->|Live Feed| DASH[Streamlit Dashboard]
    DASH -->|Export| PDF[Official Audit PDF]
    end

##  Getting Started

### Prerequisites
- **Python 3.11+**
- **Ollama** (for local LLM inference)
- **Streamlit** (for the UI)

### Installation
1. Clone the repository:
   git clone [https://github.com/preethamgowda-code/AIOS-Autonomous-Kernel.git](https://github.com/preethamgowda-code/AIOS-Autonomous-Kernel.git)
   cd AIOS-Autonomous-Kernel

2. Install dependencies:
pip install streamlit fpdf ollama

3. Pull the brain:
ollama pull llama3.2:latest

4. Running the Kernel
Start the autonomous watcher:

Bash
python core/watcher.py
Launch the executive dashboard:

Bash
streamlit run interface/dashboard.py


