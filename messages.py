import discord
import json

# List of embeded messages to clean up the code

def list_message(title):
    embed = discord.Embed(title=title,
                          description="Please enter your list items separated by ; ",
                          color=0xFF5733)
    embed.add_field(name="Example", value="Item1;Item2;Item3;Item4", inline=False)
    embed.add_field(name="Support this project",
                    value="[Donate](https://www.paypal.com/donate?hosted_button_id=QY9QSBC63TL34)",
                    inline=False)
    return embed


def timeout_message():
    embed = discord.Embed(title="No list provided within timeout!",
                          description="There is 60s timeout. ",
                          color=0xFF5733)
    embed.add_field(name="Example", value="Please start again with ?list command.", inline=False)
    return embed


def format_error_message():
    embed = discord.Embed(title="Format Error!",
                          description="Use ; separator between items! ",
                          color=0xFF5733)
    embed.add_field(name="Example", value="Please start again with ?list command.", inline=False)
    return embed


def list_exists_error_message():
    embed = discord.Embed(title="List already exists!",
                          description="Please use unique list name.",
                          color=0xFF5733)
    embed.add_field(name="Example", value="Please start again with ?list command.", inline=False)
    return embed


def guild_join_message():
    embed = discord.Embed(title="Thanks for inviting me:",
                          description="Following commands are available:",
                          color=0xFF5733)

    embed.add_field(name="?list {ListName}",
                    value="Creates new list.",
                    inline=False)

    embed.add_field(name="?random {ListName}",
                    value="Randomly selects one item from list.",
                    inline=False)

    embed.add_field(name="?delete {ListName}",
                    value="Deletes existing list.",
                    inline=False)

    embed.add_field(name="?commands",
                    value="Lists all available commands.",
                    inline=False)
    return embed


def list_created_message(title):
    embed = discord.Embed(title=title,
                          description="New list created!",
                          color=0xFF5733)
    embed.add_field(name="Support this project",
                    value="[Donate](https://www.paypal.com/donate?hosted_button_id=QY9QSBC63TL34)",
                    inline=False)
    return embed


def random_message(item):
    embed = discord.Embed(title=item,
                          description="[Support this project](https://www.paypal.com/donate?hosted_button_id=QY9QSBC63TL34)",
                          color=0xFF5733)
    return embed


def delete_message(title):
    embed = discord.Embed(title=title,
                          description="List deleted!",
                          color=0xFF5733)
    embed.add_field(name="Support this project",
                    value="[Donate](https://www.paypal.com/donate?hosted_button_id=QY9QSBC63TL34)",
                    inline=False)
    return embed


def commands_message():
    embed = discord.Embed(title="Commands:",
                          description="Following commands are available:",
                          color=0xFF5733)

    embed.add_field(name="?commands",
                    value="Lists all available commands.",
                    inline=False)

    embed.add_field(name="?delete {ListName}",
                    value="Deletes existing list.",
                    inline=False)

    embed.add_field(name="?list {ListName}",
                    value="Creates new list.",
                    inline=False)

    embed.add_field(name="?random {ListName}",
                    value="Randomly selects one item from the list.",
                    inline=False)

    embed.add_field(name="?showlists",
                    value="Prints all available lists for the user.",
                    inline=False)

    embed.add_field(name="?yesno",
                    value="Gives Yes or No answer.",
                    inline=False)

    embed.add_field(name="?8ball",
                    value="Gives random 8ball answer.",
                    inline=False)

    return embed


def print_lists_message(array, length):
    embed = discord.Embed(title="Show all lists",
                          description="Following lists are availible to you:",
                          color=0xFF5733)
    for i in range(length):
        item = array[i]
        item = json.dumps(item)
        item = item.replace('{"List_Name": "', '')
        item = item.replace('"}', '')
        embed.add_field(name=item,
                        value="\u200b",
                        inline=False)
    embed.add_field(name="Support this project",
                    value="[Donate](https://www.paypal.com/donate?hosted_button_id=QY9QSBC63TL34)",
                    inline=False)
    return embed
