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

class Contents(BaseModel):
    contents: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

#コマンドを実行するフック
@app.post("/exec")
async def exec(get_command:Command):
    return cmd.exec(get_command.cmd)

#コンテンツからPLAYBOOKを実行
@app.post("/contents_add")
async def exec(get_contents:Contents):
    command = f"ansible-playbook ./Ansible/playbooks/deploy.yml -e 'contents={get_contents.contents}'"
    return cmd.exec(command)