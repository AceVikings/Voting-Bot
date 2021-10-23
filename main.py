import discord
import os

global reactionCount,role,chosenEmoji,focusMessage
global setReaction

reactionCount = 0
role = ''
chosenEmoji = ''
client = discord.Client()
setReaction = False
focusMessage = 0
@client.event
async def on_ready():
  print("we have logged in as{0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!startVote'):
    if "craig" in [y.name.lower() for y in message.author.roles]:
      await message.channel.send("Okay boss! Choose Reaction")
      global setReaction
      setReaction = True
  if message.content.startswith('!focusMessage'):
    if "craig" in [y.name.lower() for y in message.author.roles]:
      global chosenEmoji
      if chosenEmoji == '':
        message.channel.send('You need to set an emoji first')
      else:
        global focusMessage
        focusMessage = message.id
    else:
      await message.delete()




@client.event
async def on_reaction_add(reaction,user):
  global setReaction,reactionCount,chosenEmoji
  if setReaction:
    if "craig" in [y.name.lower() for y in user.roles]:
      await reaction.message.channel.send(reaction.emoji+" has been chosen")
      setReaction = False
      chosenEmoji = reaction.emoji
    else:
      await reaction.message.remove_reaction(reaction,user)
  else:
    if focusMessage != 0:
      print("HERE")
      if "craig" in [y.name.lower() for y in user.roles]:
        print("HERE1")
        if reaction.message.id == focusMessage:
          print("HERE2")
          if reaction.emoji == chosenEmoji:
            print("HERE3")
            await reaction.message.channel.send("vote count : "+str(reaction.count))
      else:
        await reaction.message.remove_reaction(reaction,user)















client.run(os.getenv("TOKEN"))