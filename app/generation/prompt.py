def build_context(retrieved_chunks: list):
    context_blocks = []

    for chunk in retrieved_chunks:
        block = f"[Source: {chunk['source']}]\n{chunk['text']}"
        context_blocks.append(block)

    return "\n\n".join(context_blocks)