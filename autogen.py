from alembic import
from alembic.config import Config

alembic_cfg = Config("alembic.ini")
command.revision(alembic_cfg, message="autogenerate", autogenerate=True)
command.upgrade(alembic_cfg, "head")
