# Introduction
* This application is developed using Python 3.11.14.
* It was tested using OpenAI models released on June 13, 2023.
* This single user application demonstrates some concepts of a multi-tenant generative AI orchestrator and includes prompt collection templates, a user prompt response generator that uses pre-existing prompt collections and a user search memory, allowing to revisit previous stored responses produced with a particular AI model.

[![Watch the video](https://github.com/fedenolasco/ai-explains/blob/master/images/ai-explains.png)]([https://youtu.be/T-D1KVIuvjA](https://youtu.be/-gL7WHzoqms))

* [AI-explains YouTube Video](https://youtu.be/-gL7WHzoqms)

# What is a multi-tenant Gen AI orchestrator
* A multi-tenant orchestrator is an advanced system designed to manage the intricacies of deploying generative AI applications across multiple users or tenant groups. Its architecture is modular, with each component serving a specific function in the AI application workflow. Simon Attard introduced these concepts on June 20, 2023 in an article called [Leveraging Large Language Models in your Software Applications](https://medium.com/@simon_attard/leveraging-large-language-models-in-your-software-applications-9ea520fb2f34).

# Basic Installation
* This application uses Python, Streamlit UI, OpenAI API, Docker and Elasticsearch.
* Ensure you have [Git](https://git-scm.com/downloads) installed on your machine.
* Ensure you have [Python 3.11.14](https://www.python.org/downloads/release/python-3114/) installed on your machine.
* __Optional__: Ensure you have [Docker desktop, Elasticsearch and Kibana](https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html) installed on your machine. If you don't use elasticsearch you won't be able to use the __Search memory__ feature of this application.
* __Optional__: Use [Visual Studio Code](https://code.visualstudio.com/) Application as your coding environment.

## Clone Repository
* __git clone https://github.com/fedenolasco/ai-explains.git__ to your local coding folder.

## Create virtual environment for ai-explain app
* /path/to/python3.11.14 -m venv ai-explain
* Other python versions have not been tested but may run just fine.

### Windows Command
If you used the built-in venv module to create the virtual environment, you would activate it using Command Prompt:
```
ai-explain\Scripts\activate.bat
```
If you use PowerShell you would activate it using:
```
.\ai-explain\Scripts\Activate.ps1
```
### Linux or macOS
If you use bash (or similar) shell, use:
```
source ai-explain/bin/activate
```

## Install Requirements file in ai-explain
* Go to your application folder.
```
(ai-explain) path/to/ai-explain>
```
* Install dependencies from requirements.txt file
```
pip install -r requirements.txt
```
* Verify installation
```
pip list
```
## Setup .env file
All ES parameters relate to Elasticsearch installation and must be set when __ES_INSTALLED__=True.

* Use .env.example file. Rename file to ".env".
* __OPENAI_API_KEY__= # your API Key from ([platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))
* __ES_CA_CERT_PATH__=C:/path/to/config/http_ca.crt # In docker under elasticsearch container the http_ca.crt is located under /usr/share/elasticsearch/config/certs/.
* Take a copy of it and store it in your local machine and change the path of ES_CA_CERT_PATH in the .env file
* __ES_USER__= # (username of elastic user)
* __ES_PASSWORD__= # (password of elastic user)
* __ES_INSTALLED__=False # (If you don't install Elasticsearch keep "False", otherwise change to "True")
* __ES_INDEX__=searchmemory # (This is the elasticsearch default´s index name)

## Running the application
* Activate Virtual Environment ai-explain
* From the root folder run streamlit app
```
(ai-explain) path/to/ai-explain> streamlit run "1_Concept and Architecture.py" 
```
# Opensource Community
As we stand on the cusp of a new era in human-AI collaboration, the Single User AI Orchestrator Application offers a glimpse into the future of personalized and efficient interactions with generative AI systems. However, the vision is far grander—a robust, scalable, and secure multi-tenant orchestrator capable of serving diverse user needs across various domains. Achieving this vision is not a solitary endeavor but a collaborative one.

I extend a warm invitation to the open-source community to join me in this exciting journey. Your expertise in design, architecture, and software development can immensely contribute to building a software stack that is not only more robust but also capable of supporting a multi-tenant orchestrator. Together, we can push the boundaries of what is possible in the realm of generative AI, building tools that are not only powerful but also ethical, responsible, and inclusive.

Thank you for your interest, and I look forward to your valuable contributions to this project.

Feel free to connect with the author via [GitHub](https://github.com/fedenolasco) or [Linkedin](https://www.linkedin.com/in/federiconolasco/).



