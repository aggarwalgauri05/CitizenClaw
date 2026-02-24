# pdf-reader Skill

This skill provides secure access to reading PDF documents from an approved directory.

## Functionality

1.  **Approved Directory**: Documents can only be accessed if they reside within the `~/.openclaw/workspaces/default/docs/govt-policies` directory.
2.  **File Access Control**: The script enforces strict access control. Any attempt to read a file outside this directory will be blocked.
3.  **Argument Handling**:
    *   `--file <PATH>`: Specifies the PDF file to read.
    *   `--query <TEXT>` (optional): A search term to find the most relevant section within the PDF.
    *   `--list` (flag): Lists all PDF files available in the approved directory.

## Behaviour

-   **Directory Validation**: The script checks if the provided file path is within the `~/.../govt-policies/` directory.
    -   If outside: Prints `[BLOCKED] File outside approved documents directory` and exits with an error.
    -   If inside: Prints `[ALLOWED] Reading approved policy document: <filename>`.

-   **Listing PDFs (`--list`)**:
    -   Lists all files found in the `~/.openclaw/workspaces/default/docs/govt-policies/` directory.

-   **Reading and Querying (`--file` + `--query`)**:
    -   Opens the specified PDF file using `pymupdf`.
    -   Searches for the `--query` text within the document.
    -   Extracts and prints the first 4000 characters of the most relevant content found. Relevance is determined by finding pages that contain the query.
    -   Prints the source information: `[SOURCE] Official document: <filename>`.

-   **Dependencies**: Requires the `pymupdf` (fitz) Python library to be installed.

## Usage

**To list available PDFs:**
```bash
python read_pdf.py --list
```

**To read a PDF and search for content:**
```bash
python read_pdf.py --file <path/to/policy.pdf> --query "your search term"
```

Replace `<path/to/policy.pdf>` with the actual path to a PDF within the approved directory and `"your search term"` with your query.

---

**Note**: This SKILL.md only describes the contract for the skill. The actual implementation is in `read_pdf.py`.
