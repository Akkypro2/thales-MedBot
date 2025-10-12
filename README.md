# MedBot
An AI-powered educational medical chatbot designed for medical students and individuals seeking health-related information. Unlike general-purpose chatbots, this system is strictly focused on the medical domain, ensuring responses stay relevant, reliable, and educational.  

*Android Frontend* - A simple and intuitive mobile interface for users to interact with the chatbot.<br>
*RAG Backend* - A robust AI engine that retrieves medical knowledge from curated sources and generates meaningful answers.  

# Description
MedBot is an LLM-powered multimodal chatbot prototype designed to assist with queries in the medical domain. Built on a Retrieval-Augmented Generation (RAG) framework, it combines intelligent information retrieval with generative capabilities to provide accurate, context-aware responses.

## ⚙️ Key Features
🩺 Medical Expertise – Specialized on curated medical datasets covering topics like human anatomy, diseases, medications, and physiological functions.

🔍 Retrieval-Augmented Generation (RAG) – Enhances accuracy and factual grounding by retrieving relevant medical information before generating responses.

🧩 Multimodal Understanding – Capable of interpreting and explaining medical images, charts, and diagrams.

🧠 Session Memory – Incorporates short-term memory to retain context within a conversation session for more coherent interactions.

🚫 Content Safety – Includes abusive language detection and filtering, ensuring safe and respectful communication.

## ⚙️ Tech Stack
📱 Frontend – Android Studio

🎨 UI – Jetpack Compose

🔗 Networking – Retrofit

🔒 Auth – Firebase + Google

🤖 LLM – Google Gemini

🧭 Retrieval – RAG + FAISS

🔡 Embeddings – Hugging Face

⚡ Backend – FastAPI

🌐 Tunneling – Ngrok

# Directory Structure
## Backend
```bash
backend/
│── data                      # contains pdf/data sources
│── src/
    │── api.py                #  entrypoint of the project
    │── embed.py              #  defines the embedding
    │── ingest.py             #  load and split documents
    │── ingest_index.py       #  script for initial setup for loading and storing
    │── rag_pipeline.py       #  defines the rag pipeline
    │── vector_store.py        #  create, save and load vector store
requirements.txt              #  requirements for the project
```
## Frontend    
```bash
GeminiChatBot/
├── app/
│   ├── manifests/
│   │   └── AndroidManifest.xml                    # Declares app components and permissions
│   │
│   ├── kotlin+java/
│   │   └── com/example/geminichatbot/
│   │       ├── ui/theme/                          # Contains application interfaces and different screens
│   │       │   ├── AuthViewModel.kt               # Contains authentication logic and state
│   │       │   ├── ChatPage.kt					   # Main chat screen UI
│   │       │   ├── Color.kt					   # App color scheme definition
│   │       │   ├── LoginPage.kt				   # User Login UI
│   │       │   ├── MyAppNavigation.kt		       # App navigation setup
│   │       │   ├── Theme.kt				       # Centralised theme management 
│   │       │   └── Type.kt				           # Typography and text styles
│   │       │
│   │       ├── ChatViewModel.kt                   # Manages chat messages and API calls
│   │       ├── Constants.kt					   # Stores global constants like API key and URL
│   │       ├── MainActivity.kt					   # Entry point of the app 
│   │       ├── MedicalChatApi.kt				   # Retrofit interface 
│   │       ├── MedicalQueryRequest.kt			   # Model for outgoing queries
│   │       ├── MedicalQueryResponse.kt			   # Model for handling API responses
│   │       ├── MessageModel.kt					   # Data class for chat messages
│   │       └── RetroFitClient.kt				   # Configures Retrofit client and base URL
│   │
│   ├── com/example/geminichatbot/ (androidTest)
│   │   └── ExampleInstrumentedTest.kt
│   │
│   ├── com/example/geminichatbot/ (test)
│   │   └── ExampleUnitTest.kt
│   │
│   └── res/
│       ├── drawable/
│       ├── font/
│       ├── mipmap/
│       ├── values/
│       ├── xml/
│       │   ├── backup_rules.xml
│       │   ├── data_extraction_rules.xml
│       │   └── network_security_config.xml		     # Network and SSL configuration
│       └── res/ (generated)
│
├── Gradle Scripts/
│   ├── build.gradle.kts (Project: GeminiChatBot)
│   ├── build.gradle.kts (Module: app)	             # App module dependencies and plugins
│   ├── proguard-rules.pro
│   ├── gradle.properties
│   ├── gradle-wrapper.properties
│   ├── libs.versions.toml
│   ├── local.properties
│   └── settings.gradle.kts
│
└── gradle/
    └── wrapper/
        └── gradle-wrapper.jar
```
# Installation
## Requisites
```bash
Android Studio Narwhal 3 Feature Drop | 2025.1.3
Python3.x 
GOOGLE APPLICATION CREDENTIALS
LangChain 0.3.x
```

## Step 1 - Clone the repository
```bash
git clone https://github.com/the-flying-cow/thales-medbot.git
cd thales-MedBot
```
## Step 2 -Setup Backend
### -> Navigate to backend folder
```bash
cd backend
```
### -> Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
### -> Install the requirements
```bash
pip install -r requirements.txt
```
#### Create a .env file in the backend directory
Add the following to it
```bash
GOOGLE-API-KEY=your-api-key
VECTORSTORE_PATH=./vectorstore
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account.json
```
### -> Running the server
#### If running frontend and backend on different devices
```bash
uvicorn src.api:app --reload --host 0.0.0.0 --port 8000
```
In a different terminal run
```bash
ngrok http 8000
```
#### If running frontend and backend on same devices
```bash
uvicorn src.api:app --reload --host 127.0.0.1 --port 8000
```
## Step 3 -Setup Frontend
Open the frontend directory in Android Studio and run the app.
