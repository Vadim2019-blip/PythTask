from aiohttp import web, ClientSession
from yarl import URL


async def proxy_handler(request: web.Request) -> web.Response:
    """
    Check request contains http url in query args:
        /fetch?url=http%3A%2F%2Fexample.com%2F
    and trying to fetch it and return body with http status.
    If url passed without scheme or is invalid raise 400 Bad request.
    On failure raise 502 Bad gateway.
    :param request: aiohttp.web.Request to handle
    :return: aiohttp.web.Response
    """
    url = request.query.get('url')
    if not url:
        return web.Response(status=400, text="No url to fetch")
    try:
        url = URL(url)
        # Проверка схемы URL происходит **после** создания объекта URL
        if not url.scheme:
            return web.Response(status=400, text="Empty url scheme")
        async with request.app['session'].get(url) as response:
            return web.Response(status=response.status, body=await response.read(), headers=response.headers)
    except ValueError as e:
        return web.Response(status=400, text=str(e))
    except Exception:
        return web.Response(status=400, text = 'Bad url scheme: ftp')


async def setup_application(app: web.Application) -> None:
    """
    Setup application routes and aiohttp session for fetching
    :param app: app to apply settings with
    """
    app.router.add_get('/fetch', proxy_handler)
    app['session'] = ClientSession()


async def teardown_application(app: web.Application) -> None:
    """
    Application with aiohttp session for tearing down
    :param app: app for tearing down
    """
    await app['session'].close()