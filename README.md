# AI stylist
## LLM based aplication to find what suits you

## RUN
1. cd AI-stylist
2. touch .env
3. fill .env with your credentials like in .env.example
4. sudo docker-compose up --build -d

## REDIS scheme
`conversation_id` - Key to get conversation history
Inside it:
    [ # `Usual Open AI scheme`
        "content": '{ # `But the content is stored as a string`
            "role": "system" / "user" / "assistant",
            "content": [
                {
                    "type": "text" / "image_url",
                    "text" / "image_url": "example text" / "example image url"
                },
                ...
            ]
        }',
        ...
    ]
