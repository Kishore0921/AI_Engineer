'''import tiktoken

def analyze_text(text, encoding_name="cl100k_base"):
    # Load the target token encoder pattern (cl100k_base is used by gpt-4o-mini / gpt-4)
    encoder = tiktoken.get_encoding(encoding_name)
    
    # Calculate counts
    word_count = len(text.split())
    tokens = encoder.encode(text)
    token_count = len(tokens)
    
    return word_count, token_count, tokens

def main():
    # Comparing sentences to show token structure changes (e.g. spaces, rare words, syntax punctuation)
    sentences = [
        "Python is an awesome language for building AI infrastructure apps.",
        "PythonIsAwesomeForAIInfrastructureApps!",
        "def parse_data(items):\n    return [item.strip() for item in items if item]"
    ]

    print("==========================================================================")
    print("                        PYTHON TOKEN-COUNTING TOOL                        ")
    print("==========================================================================")

    for idx, text in enumerate(sentences, 1):
        words, tokens, token_ids = analyze_text(text)
        print(f"\n[Sentence {idx}]: \"{text.replace('\n', ' [newline] ')}\"")
        print(f"  - Word Count:  {words}")
        print(f"  - Token Count: {tokens}")
        print(f"  - Raw Token IDs: {token_ids[:8]}..." if len(token_ids) > 8 else f"  - Raw Token IDs: {token_ids}")
        print("-" * 60)

if __name__ == "__main__":
    main()
'''
# needs some dependencies and installation so its in multiline commenting way