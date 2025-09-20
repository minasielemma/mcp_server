from fastapi import FastAPI
from api.v1 import auth, mcp
from db.database import Base, engine
import uvicorn
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MCP Server with JWT Auth")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(mcp.router, prefix="/mcp", tags=["mcp"])

@app.get("/")
def root():
    return {"msg": "MCP Server is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
