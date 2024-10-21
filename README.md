# ScrapeBiblio: PDF Reference Extraction and Verification Library

## Powered by Scrapegraphai
![ScrapeBiblio Logo](docs/scrapebiblio.png)
[![Downloads](https://static.pepy.tech/badge/scrapebiblio)](https://pepy.tech/project/scrapebiblio)

ScrapeBiblio is a powerful library designed to extract references from PDF files, verify them against various databases, and convert the content to Markdown format.

## Features

- Extract text from PDF files
- Extract references using OpenAI's GPT models
- Verify references using Semantic Scholar, CORE, and BASE databases
- Convert PDF content to Markdown format
- Integration with ScrapeGraph for additional reference checking

## Installation

Install ScrapeBiblio using pip:
```bash
pip install scrapebiblio
```

## Configuration

Create a `.env` file in your project root with the following content:

```plaintext
OPENAI_API_KEY=your_openai_api_key
SEMANTIC_SCHOLAR_API_KEY=your_semantic_scholar_api_key
CORE_API_KEY=your_core_api_key
BASE_API_KEY=your_base_api_key
```
## Usage

Here's a basic example of how to use ScrapeBiblio:

```python
from scrapebiblio.core.find_reference import process_pdf
from dotenv import load_dotenv
import os
load_dotenv()
pdf_path = 'path/to/your/pdf/file.pdf'
output_path = 'references.md'
openai_api_key = os.getenv('OPENAI_API_KEY')
semantic_scholar_api_key = os.getenv('SEMANTIC_SCHOLAR_API_KEY')
core_api_key = os.getenv('CORE_API_KEY')
base_api_key = os.getenv('BASE_API_KEY')
process_pdf(pdf_path, output_path, openai_api_key, semantic_scholar_api_key,
core_api_key=core_api_key, base_api_key=base_api_key)
```
## Advanced Usage

ScrapeBiblio offers additional functionalities:

1. Convert PDF to Markdown:
```python
from scrapebiblio.core.convert_to_md import convert_to_md
convert_to_md(pdf_path, output_path, openai_api_key)
```
2. Check references with ScrapeGraph:

```python
from scrapebiblio.utils.api.reference_utils import check_reference_with_scrapegraph
result = check_reference_with_scrapegraph("Reference Title")
```
## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.