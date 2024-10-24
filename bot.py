#from dotenv import load_dotenv
import os
import discord

from bot_functions import location
#load_dotenv()
Token = "MTExNDY0NDczODIxNDIwNzU4OA.Gcx7VZ.W7rdiL06Rj3WZhxIOe8KTfvZvaiYJ8jfT1TE9A" #os.getenv("token")

# gives permissions to bot
intents = discord.Intents.all()


class Bot(discord.Client):
    async def on_ready(self):
        print("bot on")

    async def on_message(self, message):
        print(
            f"message found: {message.content} from {message.author} in {message.channel}")
        if message.author == client.user:
            return
        if "hello" in message.content.lower():
            print(f"command recognized: hello")
            await message.channel.send("hello")

        if message.content == "react":
            print("react command recognized")
            await message.channel.send("reacted")

        async def on_typing(self, channel, user, when):
            print(f"{user} is typing in {channel} at {when}")
            await channel.send(f": see you typing, {user}")
    # places
        if 'find' in message.content.lower():
            # find (search_string)(verb)(location)
            message_list = message.content.lower().split()

            index = message_list.index("find")
            # set search string
            search_string = ""
            index += 1
            print(message_list)
            preference = "popularity"
            while (message_list[index] != " near" or message_list[index] != "in") and index+1 < len(message_list):
                search_string = search_string + message_list[index]
                

            # set preference
                print(message_list[index])
                if message_list[index] == "near":
                    preference = "distance"
                    #print("set preference to distance")
                index += 1
            #preference = "popularity"
           # index += 1

            # set location
            loc = ""
            while index < len(message_list):
                if index != len(message_list)-1:
                    loc += message_list[index] + " "
                else:
                    loc += message_list[index]
                index += 1
                print(loc, search_string,preference)
            await message.channel.send(location.find_places_nearby(loc, search_string, preference))

        if 'where' in message.content.lower():
            await message.channel.send(location.get_location("philadelphia"))

    async def on_typing(self, channel, user, when):
        print(f"{user} is typing in {channel} at {when}")
        await channel.send(f"I see you typing, {user}")


# create instance of client class with intents parameters
client = Bot(intents=intents)
client.run(Token)
