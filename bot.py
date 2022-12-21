from pyrogram import Client, filters


bot = Client(
    'Bot', 
    api_id = 16756774, 
    api_hash ='9bc4030d639c431fae3383c0427bf0ee', 
    bot_token ='5829316810:AAHu15gMm8Js9f6Hj1o-YfAwrbjgh2p5pA0'
)



@bot.on_message(filters.command('start'))
def start(bot,msg):
    bot.send_message(msg.chat.id, 'hello Word' )

bot.run()



    
