from aiohttp import web

async def handle(request):
    return web.Response(text="Bot çalışıyor!")

app = web.Application()
app.add_routes([web.get('/', handle)])

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=10000)
