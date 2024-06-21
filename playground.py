import random
import discord
from discord.ext import commands


token = None


def load_token():
    global token
    token_file = open("token.txt").read()

    token = token_file


TESTING_GUILD = 'Egmonts Information Center'
TESTING_CHANNEL_ID = 1251943637059633183

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def commands():
    @client.command()
    async def command_list(ctx):
        embed = discord.Embed(title="Commands")
        embed.add_field(name="!info", value="Shows info about the bot", inline=False)
        embed.add_field(name="!users", value="Shows how many members the server has", inline=False)
        embed.add_field(name="!rps <your choice>", value="Play a game of rock, paper, scissors!")
        embed.add_field(name="!reversify <your text>", value="Reverses your text.")
        embed.add_field(name="!morse <your text>", value="Translates your text into morse code!")
        await ctx.send(content=None, embed=embed)

    @client.command()
    async def info(ctx):
        await ctx.send(f"A testing bot.\n\nMade by *egmont11*")

    @client.command()
    async def users(ctx):
        await ctx.send(f"""This server has {"id.member_count"} members""")  # TODO: nějak dostat sem počet uživatelů

    @client.command(name="rps")
    async def rock_paper_scissors(ctx, arg):
        players_win = False
        players_loss = False
        tie = False

        bots_choice = random.randint(1, 3)

        if arg == "rock" or arg == "Rock":
            arg = "Rock"
            if bots_choice == 1:
                tie = True
            elif bots_choice == 2:
                players_loss = True
            elif bots_choice == 3:
                players_win = True

        if arg == "paper" or arg == "Paper":
            arg = "Paper"
            if bots_choice == 2:
                tie = True
            elif bots_choice == 3:
                players_loss = True
            elif bots_choice == 1:
                players_win = True

        if arg == "scissors" or arg == "Scissors":
            arg = "Scissors"
            if bots_choice == 3:
                tie = True
            elif bots_choice == 1:
                players_loss = True
            elif bots_choice == 2:
                players_win = True

        if bots_choice == 1:
            bots_choice = "Rock"
        elif bots_choice == 2:
            bots_choice = "Paper"
        elif bots_choice == 3:
            bots_choice = "Scissors"

        if players_win:
            game_result = f"Player chose: {arg}\nBot chose: {bots_choice} \n\n*The player has won!*"
        if players_loss:
            game_result = f"Player chose: {arg}\nBot chose: {bots_choice} \n\n*The bot has won!*"
        if tie:
            game_result = f"Player chose: {arg}\nBot chose: {bots_choice} \n\n*it's a tie!*"

        await ctx.reply(game_result)

    @client.command(name="reversify")
    async def reverse_string(ctx, arg):
        string = ""
        string_list = []

        for letter in arg:
            string_list.append(letter)

        string_list.reverse()
        index = 0

        for letter in string_list:
            string += string_list[index]
            index += 1

        await ctx.reply(string)

    @client.command(name="morse")
    async def morse_code_translation(ctx, arg):
        string = translate_letter_to_morse(arg)

        await ctx.reply(f"{string} \ncurrently has some issues")


def translate_letter_to_morse(string):      # not fixed yet
    print("beggining")
    for letter in string:
        if letter != ' ':
            letter.upper()
            to_be_added = MORSE_CODE_DICT[letter]
            string += to_be_added
            print("added letter")
        else:
            string += ' '
    print("finished with the string")
    return string


def main():
    load_token()
    commands()  # initiates the commands
    client.run(token)  # turns the bot on


if __name__ == "__main__":
    main()
