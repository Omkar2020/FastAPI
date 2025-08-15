from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class Language(str, Enum):
    PY = 'Python'
    JS = 'JavaScript'
    GO = 'Go'
    JAVA = 'Java'


class Blog(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: bool
    language : Language = Language.PY
    #created_at: datetime = datetime.now()
    created_at: datetime = Field(default_factory=datetime.now)

blog=Blog(title='My First Blog', is_active=False)
print(blog)    
    
import time
time.sleep(10)  # Simulating a delay to show created_at timestamp change

again_blog=Blog(title='My Second Blog', description='This is a blog about Python', is_active=True, language=Language.JS)
print(again_blog)   

print ("//we can not add Dynamic fields such as Datetime like above")
print("//to avoid such situation we can use Field with default_factory")


