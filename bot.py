from dotenv import load_dotenv
import os
import discord

from bot_functions import location
load_dotenv()
Token = os.getenv("bot_token") 

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
            await message.channel.send("Hello!, use !help for a list of commands!")

        if message.content == "react":
            print("react command recognized")
            await message.channel.send("reacted")

        async def on_typing(self, channel, user, when):
            print(f"{user} is typing in {channel} at {when}")
            await channel.send(f": see you typing, {user}")
    # places
        if '!help' in message.content.lower():
            await message.channel.send("Commands: "+"\n"+ "Where is the airport / terminal"+"\n"+"Security Info")
        if 'security' in message.content.lower():
            await message.channel.send("Security requirements for Philadelphia Airport are:"+"\n"+"Boarding Pass"+"\n"+"Photo ID"+"\n"+"Liquids/gels/aerosols must be less than 3.4 ounces and fit in a 1qt sized bag "+"\n"+"Carry-on bags must be less than 35 lbs and no more than 10”x16”x24” in size "+"\n"+"Checked bags must be less than 40 lbs and no longer than 62” "+"\n"+"All firearms must be unloaded and in checked bags " )
        if 'find' in message.content.lower():
            # find (search_string)(verb)(location)
            message_list = message.content.lower().split()

            index = message_list.index("find")
            # set search string
            search_string = ""
            index += 1
           # print(message_list)
            preference = "popularity"
            while (message_list[index] != " near" or message_list[index] != "in") and index+1 < len(message_list):
                search_string = search_string + message_list[index]
            # set preference
                #print(message_list[index])
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
                #print(loc, search_string,preference)
            await message.channel.send(location.find_places_nearby(loc, search_string, preference))

        if 'where' in message.content.lower():
            message_list = message.content.lower().split()

            index = message_list.index("where")
            # set search string
            if 'terminal' in message_list:
                await message.channel.send(file=discord.File(r'C:\Users\Mattg\random stuff\Downloads\airport.png'))
            if 'airport' in message_list:
                await message.channel.send("8500 Essington Ave, Philadelphia, PA 19153")
            
            # search_string = ""
            # index += 1
            # while (message_list[index]!= 'terminal' or message_list[index]!= 'airport') and index <= len(message_list):
            #     index+=1
            # if message_list[index] == 'terminal':
            #     await message.channel.send(file=discord.File(r'C:\Users\Mattg//random stuff\Downloads//airport.png'))
            # elif message_list[index] == 'airport':
            #     await message.channel.send("8500 Essington Ave, Philadelphia, PA 19153")
            #     
            # else:
            #     await message.channel.send("invalid input")
            
    async def on_typing(self, channel, user, when):
        print(f"{user} is typing in {channel} at {when}")
        await channel.send(f"I see you typing, {user}")


# create instance of client class with intents parameters
client = Bot(intents=intents)
client.run(Token)
