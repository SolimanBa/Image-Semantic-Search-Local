# Semantic Image Search

A fully local AI-powered semantic image search application built with Python, Hugging Face Transformers, Sentence Transformers, ChromaDB, and Gradio.

The system scans image folders, generates captions using a vision-language model, converts captions into vector embeddings, stores them in a local vector database, and allows natural language search over personal image collections.

Example queries:

* "person holding a snake"
* "two laptops on a desk"
* "chess board on a table"
* "mountain landscape"

Unlike traditional filename-based search, retrieval is based on semantic meaning.

---

## Features

* Recursive image folder scanning
* Automatic image caption generation using BLIP
* Text embedding generation using Sentence Transformers
* Local vector storage with ChromaDB
* Natural language semantic search
* Gradio web interface
* Persistent local storage
* Incremental indexing (previously indexed images are skipped)

---

## Architecture

```text
Images
   ↓
Scanner
   ↓
BLIP Captioning Model
   ↓
Generated Captions
   ↓
Sentence Transformer Embeddings
   ↓
ChromaDB Vector Store
   ↓
Semantic Search
   ↓
Top Matching Images
```

---

## Project Structure

```text
semantic-image-search/
│
├── app/
│   ├── scanner.py
│   ├── captioner.py
│   ├── embedder.py
│   ├── vector_store.py
│   ├── search.py
│   └── ui.py
│
├── scripts/
│   └── index_images.py
│
├── data/
│   ├── images/
│   ├── captions/
│   └── chroma_db/
│
├── notebooks/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Tech Stack

* Python
* Hugging Face Transformers
* Salesforce BLIP Image Captioning Model
* Sentence Transformers (all-MiniLM-L6-v2)
* ChromaDB
* Gradio
* Pillow

---

## How It Works

### 1. Image Scanning

The application recursively scans image folders and collects supported image files.

### 2. Caption Generation

Each image is processed by the BLIP image captioning model to generate a natural language description.

Example:

```text
Image:
Person holding a snake

Generated Caption:
"a person holding a small snake in their hand"
```

### 3. Embedding Generation

Generated captions are converted into dense vector embeddings using a Sentence Transformer model.

### 4. Vector Storage

Embeddings, captions, and image metadata are stored in a persistent ChromaDB vector database.

### 5. Semantic Search

User queries are embedded using the same embedding model and compared against stored caption embeddings using vector similarity search.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/SolimanBa/Image-Semantic-Search-Local.git
cd semantic-image-search
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Place images inside:

```text
data/images/
```

Run the application:

```bash
python main.py
```

The application will:

1. Index new images
2. Store captions and embeddings locally
3. Launch the Gradio search interface

Open the local URL displayed in the terminal.

---

## Example Queries

```text
person holding a snake
```

```text
two laptops on a desk
```

```text
chess set
```

```text
mountain view
```

---

## Future Improvements

* CLIP-based image embeddings
* SigLIP support
* OCR integration
* Face recognition
* Hybrid retrieval (caption + image embeddings)
* Metadata filtering
* Duplicate image detection
* Faster indexing pipeline
* Batch embedding generation
* Advanced ranking strategies

---

## Learning Goals

This project was built to better understand:

* Image Captioning
* Semantic Embeddings
* Vector Databases
* Retrieval Systems
* Multimodal AI
* Local AI Inference
* AI Engineering Workflows

---

## License

MIT License
