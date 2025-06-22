# 📘 Auto_Bookflow

**Auto_Bookflow** is a modular pipeline that:
1. Scrapes chapter text from an online source.
2. Uses AI to rewrite and review the content.
3. Allows human edits across multiple iterations.
4. Tracks all versions in both Markdown files and a ChromaDB vector store.
5. Lets you query or list past versions easily.

---

## 🛠️ Project Structure

Auto_Bookflow/
├── main_workflow.py # Main pipeline (scrape ➜ AI write ➜ human edit ➜ save)
├── view_versions.py # View or search saved versions
├── debug_chroma.py # ChromaDB test script
├── version_manager.py # Handles version saving, querying, and file writes
├── scrape_chapter.py # Scrapes chapter content
├── ai_writer.py # AI spinning and review logic
├── human_review.py # Terminal-based human editing interface
├── chapter1.md # Final cumulative history of all versions
├── *.md # Each version (original, ai, human_edit_v1, etc.)
├── .chroma/ # Local ChromaDB persistence directory
└── README.md

 Usage
 Run the Main Workflow
 python main_workflow.py

Server Mode 
Start a ChromaDB server:
chroma run --host localhost --port 8000 --path .chroma

Sample Output
A single run might produce:
original.md: Scraped raw chapter.
ai_writer_v1.md: AI-spun version.
ai_reviewer_v1.md: AI-reviewed version.
human_edit_v1.md: Your edited version.
chapter1.md: All human edits merged chronologically

 Credits
Created by Sai Vinil — inspired by the automation of book editing using LLMs.
