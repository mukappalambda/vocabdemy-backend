"""Example showing lifespan support for startup/shutdown with strong typing."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from datetime import datetime
from typing import cast

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

from app.db.database import Database
from app.models.vocab import Vocab


@dataclass
class AppContext:
    """Application context with typed dependencies."""

    db: Database


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context."""
    # Initialize on startup
    db = await Database.connect()
    try:
        yield AppContext(db=db)
    finally:
        # Cleanup on shutdown
        await db.disconnect()


# Pass lifespan to server
mcp = FastMCP("My App", lifespan=app_lifespan)


@mcp.tool()
def get_vocabs(ctx: Context[ServerSession, AppContext]) -> str:
    """Tool that uses initialized resources."""
    sm = ctx.request_context.lifespan_context.db.get_session_maker()
    with sm.begin() as session:
        query = session.query(Vocab)
        vocabs = query.all()
        json_str = ",".join([cast(str, vocab.vocab) for vocab in vocabs])
        return json_str


@mcp.tool()
def delete_vocab(ctx: Context[ServerSession, AppContext], vocab: str) -> str:
    """Tool to delete a vocabulary entry."""
    sm = ctx.request_context.lifespan_context.db.get_session_maker()
    with sm.begin() as session:
        query = session.query(Vocab).filter(Vocab.vocab == vocab)
        vocab_to_delete = query.first()
        if vocab_to_delete:
            session.delete(vocab_to_delete)
            session.commit()
            return f"Deleted vocab: {vocab} at {datetime.now()}"

        return f"Vocab '{vocab}' not found."
