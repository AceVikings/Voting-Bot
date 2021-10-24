import discord
import os
import re

global reactionCount,role,chosenEmoji,focusMessage
global setReaction
global roleRegex
roleRegex = re.compile(r'<@&?(\d+)>')

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        print("It's match")
        return(True) 
    print("Noup")
    return(False) 
    
global messageReactions
messageReactions = dict()
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
  global messageReactions
  messageReactions[message.id]=dict()
  messageReactions[message.id]["author"]=message.author
  message
  messageReactions[message.id]["allowedRoles"]= roleRegex.findall(message.content)
 

  
  # if(message.content.startswith('!votes')):
  #   await message.channel.send(messageReactions[message.id])
    
  # if message.content.startswith('!startVote'):
  #   if "craig" in [y.name.lower() for y in message.author.roles]:
  #     await message.channel.send("Okay boss! Choose Reaction")
  #     global setReaction
  #     setReaction = True
  # if message.content.startswith('!focusMessage'):
  #   if "craig" in [y.name.lower() for y in message.author.roles]:
  #     global chosenEmoji
  #     if chosenEmoji == '':
  #       message.channel.send('You need to set an emoji first')
  #     else:
  #       global focusMessage
  #       focusMessage = message.id
  #   else:
  #     await message.delete()




@client.event
async def on_reaction_add(reaction,user):
  global messageReactions
  if(messageReactions[reaction.message.id]["author"]==user):
    messageReactions[reaction.message.id][reaction.emoji]=int(reaction.count)
  else:
    try:
      if messageReactions[reaction.message.id][reaction.emoji] > 0:
        if(common_member(messageReactions[reaction.message.id]["allowedRoles"],[str(role.id) for role in user.roles])):
          messageReactions[reaction.message.id][reaction.emoji]=reaction.count
        else:
          await reaction.message.remove_reaction(reaction,user)
      else:
        await reaction.message.remove_reaction(reaction,user)
    except:
      await reaction.message.remove_reaction(reaction,user)

  
    
  # global setReaction,reactionCount,chosenEmoji
  # if setReaction:
  #   if "craig" in [y.name.lower() for y in user.roles]:
  #     await reaction.message.channel.send(reaction.emoji+" has been chosen")
  #     setReaction = False
  #     chosenEmoji = reaction.emoji
  #   else:
  #     await reaction.message.remove_reaction(reaction,user)
  # else:
  #   if focusMessage != 0:
  #     if "craig" in [y.name.lower() for y in user.roles]:
  #       if reaction.message.id == focusMessage:
  #         if reaction.emoji == chosenEmoji:
  #           await reaction.message.channel.send("vote count : "+str(reaction.count))
  #     else:
  #       await reaction.message.remove_reaction(reaction,user)















client.run(os.getenv("TOKEN"))