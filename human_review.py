def accept_human_edit(previous_text, version_number=None):
    print("\n📄 Preview hidden for brevity.")
    print("-" * 60)
    print("✏️ Paste your human-edited version below (or press Enter to keep unchanged):")

    user_input = input(">>> ").strip()
    final_text = user_input if user_input else previous_text

    # Append to chapter1.md
    with open("chapter1.md", "a", encoding="utf-8") as f:
        f.write(f"\n\n---\n## Human Edit v{version_number}\n")
        f.write(final_text)

    # Save a separate file for the version
    if version_number is not None:
        filename = f"human_edit_v{version_number}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_text)

    return final_text
