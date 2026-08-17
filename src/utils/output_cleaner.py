import re


def clean_llm_output(text):
    """
    Remove reasoning/thinking tags from LLM output
    and return only the final response.
    """

    # Remove everything between <think> and </think>
    text = re.sub(
        r"<think>.*?</think>",
        "",
        text,
        flags=re.DOTALL | re.IGNORECASE
    )

    return text.strip()