from utils import is_valid_response

def generate_answers(prompt, proposer1, proposer2, aggregator, logger):
    try:
        r1 = proposer1(prompt)[0]['generated_text']
        logger.info("Proposer 1: %s", r1)
    except Exception as e:
        r1 = f"[Error] {e}"
        logger.error("Error in Proposer 1: %s", e)

    try:
        r2 = proposer2(prompt)[0]['generated_text']
        logger.info("Proposer 2: %s", r2)
    except Exception as e:
        r2 = f"[Error] {e}"
        logger.error("Error in Proposer 2: %s", e)

    if not is_valid_response(r1): r1 = "❌ Invalid or empty response."
    if not is_valid_response(r2): r2 = "❌ Invalid or empty response."

    aggregation_prompt = f'''
You are a helpful assistant. Compare the two responses below and generate a simpler, better explanation suitable for a 10-year-old.

Response 1:
{r1}

Response 2:
{r2}

Final Answer:
'''
    try:
        final = aggregator(aggregation_prompt)[0]['generated_text']
        logger.info("Final Answer: %s", final)
    except Exception as e:
        final = f"[Error] {e}"
        logger.error("Error in Aggregator: %s", e)

    return r1, r2, final
