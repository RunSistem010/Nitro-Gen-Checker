# Nitro-Gen-Checker
Generador de Códigos de Nitro + Checker

print("Nitro-GenByAdosss")
print("Mi Server De Discord! https://discord.gg/4nsDgA6gJy")
import random, string, requests
f=open("Valid Nitro.txt" , "w" , encoding='utf-8')
 
while True:
 code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
 r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
 if r.status_code == 1:
    print(f"VALID | https//:discord.gift/{code}")
    f.write(f"https//:Discord.gift/{code}\n")
 else:
    print(f"INVALID | https://discord.gift/{code}")
