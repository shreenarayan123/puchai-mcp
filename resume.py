import pdfplumber

@mcp.tool(description=ResumeToolDescription.model_dump_json())
async def resume() -> str:
    """
    Reads your local resume (e.g. PDF) and returns its content as Markdown.
    """

    resume_path = Path(__file__).parent / "resume.pdf"

    if not resume_path.exists():
        return "ERROR: Resume file not found. Please ensure resume.pdf is in the server directory."

    try:
        text_content = ""
        with pdfplumber.open(resume_path) as pdf:
            for page in pdf.pages:
                text_content += page.extract_text() + "\n\n"

        if not text_content.strip():
            return "ERROR: Resume appears to be empty or could not be extracted."

        # Convert plain text to markdown headings etc. if you want, or just return raw
        markdown_resume = f"# My Resume\n\n{text_content.strip()}"
        return markdown_resume

    except Exception as e:
        return f"ERROR: Failed to read or parse resume: {e}"
