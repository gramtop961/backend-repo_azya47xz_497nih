"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogpost" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Blog-related schemas for this app

class BlogPost(BaseModel):
    """
    Blog posts for the fitness influencer portfolio
    Collection name: "blogpost"
    """
    title: str
    slug: str = Field(..., description="URL-friendly unique identifier")
    cover_image: Optional[str] = Field(None, description="URL to cover image")
    excerpt: Optional[str] = None
    content: str
    tags: Optional[List[str]] = []

class Message(BaseModel):
    """
    Contact form submissions
    Collection name: "message"
    """
    name: str
    email: EmailStr
    subject: Optional[str] = None
    message: str
