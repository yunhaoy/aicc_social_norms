from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from aicc_social_norms.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


def read_raw_sql(sql_path: str | Path) -> str:
    """Read a SQL file from the raw data directory.

    Relative paths are resolved against ``data/raw``; absolute paths are used
    as provided.
    """
    path = Path(sql_path)
    if not path.is_absolute():
        path = RAW_DATA_DIR / path

    if path.suffix.lower() != ".sql":
        raise ValueError(f"Expected a .sql file, got: {path}")

    return path.read_text(encoding="utf-8")


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Processing dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Processing dataset complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
