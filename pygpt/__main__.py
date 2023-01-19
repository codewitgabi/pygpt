import os
import openai


def runAi():
	# api-key for openai
	openai.api_key = os.environ.get("GPT_KEY")
	
	while True:
		prompt = input("$ ")
		if prompt == "exit":
			break
			
		response = openai.Completion.create(
			engine="text-davinci-003",
			prompt=prompt,
			max_tokens=4000,
			temperature=0.8,
			frequency_penalty=0.6)
		
		print(f"{response.choices[0].text}\n")
		
