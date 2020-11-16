from api.database import cursor

def formatNovel(item):
  data = {
    'type': item[0],
    'name': item[1],
    'author': item[2],
    'intro': item[3],
    'id': item[4],
    'cover': item[5],
  }
  return data

# 获取小说所有分类
def getNovelCategory():
  sql = 'SELECT type, type_id, count(type_id) FROM novel GROUP BY type_id ORDER BY type_id'
  cursor.execute(sql)
  data = cursor.fetchall()
  res = {
    'code': 200,
    'list': []
  }
  for item in data:
    res['list'].append({
      'name': item[0],
      'id': item[1],
      'count': item[2],
    })
  return res

# 根据分类获取小说
def getNovelList(type, page, pageSize):
  start = (page - 1) * pageSize
  end = page * pageSize
  sql = ''' SELECT type, name, author, intro, id, cover  FROM novel where type_id=\'%s\' and spider=1 ''' % (int(type))
  cursor.execute(sql)
  novelList = cursor.fetchall()
  res = {
    'count': len(novelList),
    'page': page,
    'pageSize': pageSize,
    'list': []
  }
  for item in novelList[start:end]:
    res['list'].append(formatNovel(item))
  print(len(novelList))
  return res

# 小说排行榜
def getNovelRank():
  sql = ''' SELECT type, name, author, intro, id FROM novel limit 10'''
  cursor.execute(sql)
  rankList = cursor.fetchall()
  res = {
    'list': []
  }
  for item in rankList:
    res['list'].append(formatNovel(item))
  print(rankList)
  return res

# 小说详情
def getNovelInfo(id):
  sql = ''' SELECT type, name, author, intro, id, cover, update FROM novel where id=\'%s\' ''' % id
  cursor.execute(sql)
  info = cursor.fetchone()
  print(info)
  res = {
    'code': 200,
    'data': formatNovel(info)
  }
  return res

# 小说章节
def getNovelChapter(id, page=1, pageSize=50):
  start = (page - 1) * pageSize
  end = page * pageSize
  sql = ''' SELECT id, title, ctime  FROM chapter where novel_id=\'%s\' limit %s, %s ''' % (id, start, end)
  cursor.execute(sql)
  chapters = cursor.fetchall()
  res = {
    'code': 200,
    'data': []
  }
  for chapter in chapters:
    res['data'].append({
      'id': chapter[0],
      'title': chapter[1],
      'ctime': chapter[2],
    })
  return res

# 小说章节内容
def getChapterContent(chapterId):
  sql = ''' SELECT id, content  FROM content where id=\'%s\' ''' % (chapterId)
  cursor.execute(sql)
  chapters = cursor.fetchone()
  res = {
    'code': 200,
    'data': {
      'chapterId': chapters[0],
      'content': chapters[1]
    }
  }
  return res
