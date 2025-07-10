import asyncio
import openai
from telegram import Bot

# Your credentials
BOT_TOKEN = "8172946320:AAEzGItIIkzJ3eE9LV0M9y1GNuQ2di3pU1E"
CHAT_ID = 7501700264
OPENAI_API_KEY = "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"

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

async def main():
    bot = Bot(token=BOT_TOKEN)

    try:
        # Request a chat completion from OpenAI
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Write a friendly greeting message for a Telegram post."}
            ],
            max_tokens=50,
        )

        generated_text = response.choices[0].message.content.strip()

        # Send the generated message to Telegram
        await bot.send_message(chat_id=CHAT_ID, text=generated_text)
        print("✅ Message sent to Telegram!")
        print("Generated message:", generated_text)

    except openai.OpenAIError as e:
        error_msg = str(e)
        print(f"⚠️ OpenAI error: {error_msg}")

        # Send error notification to Telegram
        if "insufficient_quota" in error_msg or "rate limit" in error_msg.lower():
            await bot.send_message(chat_id=CHAT_ID, text="⚠️ Sorry, OpenAI quota exceeded or rate limited. Please try later.")
        else:
            await bot.send_message(chat_id=CHAT_ID, text=f"⚠️ OpenAI error: {error_msg}")

if __name__ == "__main__":
    asyncio.run(main())
