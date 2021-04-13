import discord


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
                          description="There is 60s timeout. Try it again! ",
                          color=0xFF5733)
    return embed


def format_error_message():
    embed = discord.Embed(title="Format Error!",
                          description="Use ; separator between items! ",
                          color=0xFF5733)
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

    embed.add_field(name="?8ball",
                    value="Gives Yes or No answer.",
                    inline=False)

    embed.add_field(name="?8ball",
                    value="Gives random 8ball answer.",
                    inline=False)

    return embed

