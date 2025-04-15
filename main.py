import logging
import sqlite3
from mcp_experiment.tools import tools
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


mcp = FastMCP("MCP Experiment")

for tool in tools:
    logger.info(f"Adding tool: {tool.__name__}")
    mcp.add_tool(tool)


@mcp.resource("schema://main")
def get_schema() -> str:
    """Provide the database schema as a resource"""
    with sqlite3.connect("./dist/chinook.db") as conn:
        schema = conn.execute("SELECT sql FROM sqlite_master WHERE type='table'").fetchall()
        return "\n".join(sql[0] for sql in schema if sql[0])


@mcp.tool()
def query_data(sql: str) -> str:
    """Execute SQL queries safely"""
    with sqlite3.connect("./dist/chinook.db") as conn:
        try:
            # TODO: enforce select only
            result = conn.execute(sql).fetchall()
            return "\n".join(str(row) for row in result)
        except Exception as e:
            return f"Error: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport='stdio')
