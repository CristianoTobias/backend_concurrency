from time import sleep
import asyncio
import httpx
from django.http import HttpResponse
from django.http import JsonResponse

def api(request):
    sleep(5)
    payload = {"message": "Hello world"}
    if "task_id" in request.GET:
        payload[task_id] = request.Get("task_id")
    return JsonResponse(payload)

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

def http_call_sync():
    for num in range(1, 10):
        sleep(1)
        print(num)
    
    r = httpx.get("https://httpbin.org")
    print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    await loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")

def sync_view(request):
    http_call_sync()
    return HttpResponse("blocking HTTP request")