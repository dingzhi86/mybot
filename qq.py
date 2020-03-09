from aiocqhttp import CQHttp, ApiError
import aiohttp
import json

bot = CQHttp(api_root='http://127.0.0.1:5700/')


@bot.on_message
async def handle_msg(context):
    try:
        k = 0
        message = context.get('message')
        print(message)
        if message.find("十连") >= 0:
            k = 10
        elif message.find("单抽") >= 0:
            k = 1
        if k > 0:
            async with aiohttp.request('GET', "http://127.0.0.1:8000/lottery/" + str(context['sender']['user_id']) + "/" + str(k)) as resp:
                if 200 <= resp.status < 300:
                    contet = await resp.json()
                    names = [item["name"] for item in contet["item"]]
                    await bot.send(context, '恭喜你获得[' + ','.join(names) + ']', at_sender=True)
                    print(contet)
                    for i in  contet["collection"]:
                        await bot.send(context, '恭喜你集齐套装[' + i + ']', at_sender=True)

                elif resp.status == 404:
                    await bot.send(context, "抱歉，您的抽奖次数不足")
                else:
                    await bot.send(context, "抱歉，抽奖服务好像挂了唉!")

    except ApiError as e:
        print(e)
        await bot.send(context, "抱歉，抽奖服务好像挂了唉!!")
    except Exception as e:
        print(e)
        await bot.send(context, "抱歉，抽奖服务好像挂了唉!!!")


if __name__ == '__main__':
    bot.run(host='localhost', port=8888)
    print(bot)
