import random
import json
import asyncio
import pymongo
import messages as mes
import tokens as tok
import time

clientDB = pymongo.MongoClient(tok.mongo_token)
db = clientDB.bot


# Base class for other exceptions
class Error(Exception):
    pass


# Raised when the list format is wrong
class ListFormatError(Error):
    pass


class ListExistsError(Error):
    pass


async def list_command(client, message):
    server_name = message.guild.name
    collection = db[server_name]
    list_name = message.content.replace('?list ', '')
    title = "Creating list: " + list_name
    full_user = message.author.name + "#" + message.author.discriminator
    await message.channel.send(embed=mes.list_message(title))

    try:
        def check(m):
            # checking if awaited message is from the same user that used the command
            if full_user == m.author.name + "#" + m.author.discriminator:
                # checking if user input contains ; ... else returning Format error
                if m.content.find(";") != -1:
                    return True
                else:
                    raise ListFormatError
            else:
                return False

        if collection.find_one({"User": full_user, "List_Name": list_name}, {"List": 1, "_id": False}) is None:
            message = await client.wait_for('message', timeout=60.0, check=check)
        else:
            raise ListExistsError
    # Format error + timeout error
    except asyncio.TimeoutError:
        await message.channel.send(embed=mes.timeout_message())
    except ListFormatError:
        await message.channel.send(embed=mes.format_error_message())
    except ListExistsError:
        await message.channel.send(embed=mes.list_exists_error_message())

    #   if no errors occurred, create new list
    else:
        now = int(time.time())
        collection.insert_one(
            {"User": full_user, "List_Name": list_name, "List": message.content, "Timestamp": now})
        title = list_name + " created!"
        await message.channel.send(embed=mes.list_created_message(title))
    return


async def random_command(message):
    list_name = message.content.replace('?random ', '')
    server_name = message.guild.name
    full_user = message.author.name + "#" + message.author.discriminator
    # calling randomize function to get random item from list
    item = randomize(server_name, full_user, list_name)
    await message.channel.send(embed=mes.random_message(item))
    return


async def delete_command(message):
    list_name = message.content.replace('?delete ', '')
    server_name = message.guild.name
    collection = db[server_name]
    full_user = message.author.name + "#" + message.author.discriminator
    collection.delete_one({"User": full_user, "List_Name": list_name})
    title = list_name + " deleted!"
    await message.channel.send(embed=mes.delete_message(title))
    return


async def commands_command(message):
    await message.channel.send(embed=mes.commands_message())
    return


# retrieving random item from list
def randomize(server_name, full_user, list_name):
    collection = db[server_name]
    # query based on listname & username
    output = collection.find_one({"User": full_user, "List_Name": list_name}, {"List": 1, "_id": False})
    # adding timestamp of the latest use to the list
    now = int(time.time())
    timestamp = {"$set": {"Timestamp": now}}
    collection.update_one(output, timestamp)
    # formatting the query output
    output = json.dumps(output)
    output = output.replace('{"List": "', '')
    output = output.replace('"}', '')
    output = output.split(";")
    # selecting random item from the output
    output = random.choice(tuple(output))
    # check for when query returns null
    if output == "null":
        output = "List not found!"
    return output


async def eightball_command(message):
    answers = ("It is certain.", "It is decidedly so.", "Without a doubt.", "Yes – definitely.", "You may rely on it.",
               "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
               "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
               "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
               "Outlook not so good.", "Very doubtful.")
    item = random.choice(answers)
    await message.channel.send(embed=mes.random_message(item))
    return


async def yesno_command(message):
    answers = ("yes", "no")
    item = random.choice(answers)
    await message.channel.send(embed=mes.random_message(item))
    return


async def clean():
    col_list = db.list_collection_names()
    now = int(time.time())
    difference = now - 2592000

    # Loops through all collections and deletes those that are older than 30 days from now
    for i in range(len(col_list)):
        col = col_list[i]
        collection = db[col]
        myquery = {"Timestamp": {"$lt": difference}}
        collection.delete_many(myquery)
    return


async def print_lists(message):
    server_name = message.guild.name
    full_user = message.author.name + "#" + message.author.discriminator
    collection = db[server_name]
    query = collection.find({"User": full_user}, {"List_Name": 1, "_id": False})
    array = list(query)
    length = len(array)
    await message.channel.send(embed=mes.print_lists_message(array,length))
    return
