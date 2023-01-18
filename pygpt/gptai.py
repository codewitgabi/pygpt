import os
import openai


def runAi():
	endpoint = "https://api.openai.com/v1/completions"
	
	openai.api_key = "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"
	engines = openai.Model.list()
	
	
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
		
		print("f\n{response.choices[0].text}\n")
		
