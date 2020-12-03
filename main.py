from typing import Optional
from fastapi import FastAPI
import io, sys
from api.api import *
from fastapi.middleware.cors import CORSMiddleware
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 

app = FastAPI()
origins = [ "http://144.34.161.204", "*" ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 获取小说分类
@app.get("/getNovelCategory")
def read_NovelCategory():
  data = getNovelCategory()
  return data

# 获取小说排行榜
@app.get("/getNovelRank")
def read_NovelRank():
  data = getNovelRank()
  return data

# 根据分类获取小说
@app.get("/getNovelList")
def read_NovelList(type: int, page: int, pageSize:int):
  data = getNovelList(type, page, pageSize)
  return data

# 获取小说详情
@app.get("/getNovelInfo")
def read_NovelInfo(id: int):
  data = getNovelInfo(id)
  return data

# 获取小说章节
@app.get("/getNovelChapter")
def read_NovelChapter(id: int, page: int, pageSize: int):
  data = getNovelChapter(id, page, pageSize)
  return data

# 获取章节内容
@app.get("/getChapterContent")
def read_ChapterContent(chapterId: int):
  data = getChapterContent(chapterId)
  return data

# 搜索小说
@app.get("/searchNovel")
def get_Novel(name: str):
  data = searchNovel(name)
  return data