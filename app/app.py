from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

text_posts = {
    1: {"title": "New Post", "content": "cool test post"},
    2: {"title": "Update Log", "content": "added some new features today"},
    3: {"title": "Morning Thoughts", "content": "feeling productive this morning"},
    4: {"title": "Dev Notes", "content": "fixed a few bugs in the latest build"},
    5: {"title": "Weekend Plans", "content": "planning to relax and read a book"},
    6: {"title": "Daily Motivation", "content": "keep pushing forward no matter what"},
    7: {"title": "Code Drop", "content": "pushed a new branch to the repo"},
    8: {"title": "Quick Idea", "content": "thinking about building a new side project"},
    9: {"title": "Bug Report", "content": "found an issue with the login form"},
    10: {"title": "UI Update", "content": "tweaked button colors for better contrast"},
    11: {"title": "End of Day", "content": "wrapping things up and logging off"}
}


#endpoint /posts
@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts#json response

#endpoint /posts/{id}
@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not found")
    
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = {"title": post.title, "content": post.content}
    return new_post

