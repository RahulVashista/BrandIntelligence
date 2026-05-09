from pydantic import BaseModel


class BrandCreate(BaseModel):
    name: str
    official_domains: list[str] = []
    login_urls: list[str] = []
    keywords: list[str] = []
    aliases: list[str] = []
