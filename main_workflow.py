import asyncio
from scrape_chapter import get_chapter_markdown
from ai_writer import spin_content, review_content
from human_review import accept_human_edit
from version_manager import save_version, collection, client  # Include client to call .persist()

def append_to_markdown_file(content):
    with open("chapter1.md", "a", encoding="utf-8") as f:
        f.write(f"\n\n# Human Edit Version\n{content}")

async def main():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

    # Step 1: Scrape
    md_text = await get_chapter_markdown(url)

    # Step 2: AI Write + Review
    spun = spin_content(md_text)
    reviewed = review_content(spun)

    # Save earlier stages
    save_version(md_text, "original")
    save_version(spun, "ai_writer_v1")
    save_version(reviewed, "ai_reviewer_v1")

    # Step 3: Multiple Human Edits
    current_version = reviewed
    num_iterations = int(input("🧑‍💻 How many human edit iterations do you want? "))

    for i in range(1, num_iterations + 1):
        print(f"\n✏️ Human edit iteration {i}")
        current_version = accept_human_edit(current_version, version_number=i)
        version_id = f"human_edit_v{i}"
        save_version(current_version, version_id)
        collection.add(documents=[current_version], ids=[version_id])
        append_to_markdown_file(current_version) 
       

if __name__ == "__main__":
    asyncio.run(main())
