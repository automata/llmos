from openai import OpenAI

client = OpenAI()

def test_completion():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )
    print(completion.choices[0].message.content)


def test_vision():
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://github.com/automata/llmos/assets/49062/ac9eb5e3-a2b1-4607-a5cf-74d8e7e796ff"
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    print(response.choices[0].message.content)


def test_speach():
    pass

def test_listening():
    pass

if __name__ == "__main__":
    # test_completion()
    test_vision()