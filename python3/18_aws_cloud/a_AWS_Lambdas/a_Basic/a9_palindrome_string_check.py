import json


def lambda_handler(event, context):
    validwords = []
    invalidwords = []
    for sentence in event["sentences"]:
        sentenceList = [ch.lower() for ch in sentence if ch.isalnum()]
        if sentenceList == sentenceList[::-1]:
            validwords.append(sentence)
        else:
            invalidwords.append(sentence)

    return {
        "statusCode": 200,
        "validwords": json.dumps(validwords),
        "invalidwords": json.dumps(invalidwords),
    }


"""
event Data:

    {
    "sentences": [
        "A man, a plan, a canal, Panama!",
        "race a car",
        "No 'x' in 'Nixon'",
        "I like big butts and I cannot lie",
        "Was it a car or a cat I saw?",
        "Yo, banana boy!",
        "No 'x' in 'Nixon'",
        "I like big butts",
        "Was it a car or a cat I saw?"
    ]
    }
"""
