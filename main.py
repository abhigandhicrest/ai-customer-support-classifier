from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

print("===================================")
print("SENTIMENT ANALYSIS CLASSIFIER")
print("===================================")

while True:
    message = input("\n Santance: ")

    if len(message) == 0:
        message="hello"

    if message.lower() == "exit":
        print("===================================")
        print("See you later..!")
        print("===================================")

        break

    result = classifier(message)

    print(message)
    print(result)