def evaluate_answer(answer, context):
    """
    Simple evaluation to check whether the answer
    is supported by the retrieved context.
    """

    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())

    matching_words = answer_words.intersection(context_words)

    if len(matching_words) >= 3:
        return {
            "supported": True,
            "message": "The answer is supported by the retrieved context."
        }

    return {
        "supported": False,
        "message": "The answer may not be fully supported by the retrieved context."
    }