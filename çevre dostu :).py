import discord
import time
import random
from datetime import datetime
from discord.ui import Button, View
from discord.ext import commands
import os, random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
    

@bot.command()
async def çevre(ctx, bilgi=""):
    if bilgi == "":
        await ctx.send("Çevre, doğal yaşamı ve insanların yaşadığı, etkileşimde bulunduğu, çevresel faktörlerin bir araya geldiği tüm ortamları ifade eder. Çevre, biyotik (canlı) ve abiyotik (cansız) bileşenlerden oluşur.")
    elif bilgi == "sorunlar":
        await ctx.send("## Çevre Sorunları")
        await ctx.send(" - **Kirlilik:** Hava, su ve toprak kirliliği, canlıların sağlığını tehdit eder ve ekosistemleri bozar.")
        await ctx.send(" - **İklim Değişikliği:** Küresel ısınma ve iklim değişikliği, çevresel dengenin bozulmasına neden olur.")
        await ctx.send(" - **Ormansızlaşma:** Ağaçların kesilmesi, biyolojik çeşitliliğin azalmasına ve karbon döngüsünün bozulmasına yol açar.")
        await ctx.send(" - **Doğal Kaynakların Tükenmesi:** Aşırı tüketim, yenilenemez doğal kaynakların hızla tükenmesine neden olur.")
    elif bilgi == "çözümler":
        await ctx.send("Hangi çözüm türünü öğrenmek istiyorsunuz?")
        button1=Button(label="Kirliliği Azaltma",style=discord.ButtonStyle.green)
        button2=Button(label="İklim Değişikliği ile Mücadele",style=discord.ButtonStyle.green)
        button3=Button(label="Biyolojik Çeşitliliği Koruma",style=discord.ButtonStyle.green)
        button4=Button(label="Sürdürülebilir Tüketim ve Üretim",style=discord.ButtonStyle.green)
        page=0
        async def button1_callback(interaction):
            await ctx.send("## Kirliliği Azaltma")

            await ctx.send("**Hava Kirliliği:**")

            await ctx.send(" * Fosil yakıt kullanımını azaltarak ve yenilenebilir enerji kaynaklarına yönelerek hava kirliliğini azaltabiliriz.")
            await ctx.send(" * Toplu taşıma araçlarını kullanmak, bisiklete binmek ve yürümek gibi alternatif ulaşım yöntemleri tercih edilebilir.")
            await ctx.send(" - Endüstriyel tesislerde filtre ve temizleyici sistemlerin kullanılması sağlanabilir.")

            await ctx.send("**Su Kirliliği:**")

            await ctx.send(" * Atık suların arıtılarak doğaya salınması sağlanabilir.")
            await ctx.send(" - Tarımda kullanılan kimyasal gübre ve pestisitlerin kontrolü ve azaltılması teşvik edilebilir.")
            await ctx.send(" - Sanayi atıklarının düzenli ve güvenli bir şekilde bertaraf edilmesi sağlanabilir.")

            await ctx.send("**Toprak Kirliliği:**")

            await ctx.send(" * Kimyasal gübre ve pestisit kullanımını azaltarak organik tarıma yönelim sağlanabilir.")
            await ctx.send(" - Katı atıkların geri dönüştürülmesi ve düzenli depolama alanlarının kullanılması teşvik edilebilir")

        async def button2_callback(interaction):
            await ctx.send("")
     
        button1.callback= button1_callback
        button2.callback= button2_callback
        view=View()
        view.add_item(button1)
        view.add_item(button2)
        await ctx.send(view=view)
            

  
bot.run("BOT-TOKEN")
