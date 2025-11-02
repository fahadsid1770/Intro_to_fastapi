from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/external-data")
async def get_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
    return response.json()



# avoid blocking operations in async functions: 
import time
from fastapi.concurrency import run_in_threadpool

def cpu_bound_task():
    time.sleep(1)
    return "Task completed"

@app.get("/cpu-task")
async def handle_cpu_task():
    result = await run_in_threadpool(cpu_bound_task)
    return {"result": result}

