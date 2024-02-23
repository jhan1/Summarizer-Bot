from openai import AsyncOpenAI, OpenAI

# read in the token
f = open("./chatgpt_token",'r')
key = f.readlines()[0] 
OpenAI.api_key = key

# setup for chatGPT API
client = AsyncOpenAI(
    api_key=key,
)

# returns summarized text after taking in a comment tree
async def summarize_text(text_to_summarize):
    prompt = f"Summarize the comments in this text conversation tree succinctly. Ignore all usernames in the summary: {text_to_summarize}"
    client = AsyncOpenAI()
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt}
        ],
    )

    summary = response.choices[0].message.content
    return summary
