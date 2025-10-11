# MedBot
An AI-powered educational medical chatbot designed for medical students and individuals seeking health-related information. Unlike general-purpose chatbots, this system is strictly focused on the medical domain, ensuring responses stay relevant, reliable, and educational.  

*Android Frontend* - A simple and intuitive mobile interface for users to interact with the chatbot.<br>
*RAG Backend* - A robust AI engine that retrieves medical knowledge from curated sources and generates meaningful answers.  

# Description


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
    │──vector_store.py        #  create, save amd load vector store
requirements.txt              #  requirements for the project
```
## Frontend    
```bash
GeminiChatBot/
├── app/
│   ├── manifests/
│   │   └── AndroidManifest.xml                    #Declares app components and permissions
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
