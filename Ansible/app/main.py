from fastapi import FastAPI
from util import command as cmd
from util import log
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORSを回避するために追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

class Command(BaseModel):
    cmd: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/exec")
async def exec(get_command:Command):
    """トークン発行"""
    return cmd.exec(get_command.cmd)