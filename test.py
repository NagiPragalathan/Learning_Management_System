import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an algorithum and code for add two numbers",
  temperature=0.5,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["You:"]
)

print(response.choices[0].get("text"))

