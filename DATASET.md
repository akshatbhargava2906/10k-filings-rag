# Dataset: 10-K SEC Filings

This project uses the [`winterForestStump/10-K_sec_filings`](https://huggingface.co/datasets/winterForestStump/10-K_sec_filings)
dataset from the Hugging Face Hub. The data is **not committed to this repo** (it is
~13 GB compressed / ~29 GB on disk) and is git-ignored. Download it locally using one
of the methods below.

## About the data

- **Source:** [winterForestStump/10-K_sec_filings](https://huggingface.co/datasets/winterForestStump/10-K_sec_filings)
- **Content:** ~93.5K 10-K SEC EDGAR filings since 1999, split into sections
  (Business, Risk Factors, Properties, Legal Proceedings, MD&A, Financial Statements, etc.)
- **Format:** Parquet, 52 splits (`001`–`052`), ~13.4 GB download, ~29 GB uncompressed
- **Note:** The dataset contains some badly-parsed filings and empty rows — clean before use.

### Schema (key columns)

| Column          | Type             | Description                       |
| --------------- | ---------------- | --------------------------------- |
| `cik`           | int64            | SEC Central Index Key             |
| `company_name`  | string           | Filing company name               |
| `filing_date`   | timestamp[ns]    | Date of filing                    |
| `Business`      | string           | Item 1 — Business                 |
| `Risk Factors`  | string           | Item 1A — Risk Factors            |
| `Properties`    | string           | Item 2 — Properties               |
| ...             | string           | Remaining 10-K items as columns   |

---

## Option 1 — Hugging Face CLI (recommended)

Install the CLI:

```bash
pip install -U "huggingface_hub[cli]"
```

Download the full dataset into a local `./data` folder:

```bash
hf download winterForestStump/10-K_sec_filings \
  --repo-type dataset \
  --local-dir ./data
```

> On older `huggingface_hub` versions the command is `huggingface-cli download` with the
> same arguments.

### Download only specific splits (saves space/time)

Each split is a single parquet file under `data/`. Use `--include` glob patterns to
grab just what you need:

```bash
# Just splits 001 and 002
hf download winterForestStump/10-K_sec_filings \
  --repo-type dataset \
  --local-dir ./data \
  --include "data/001-*" "data/002-*"
```

### Faster downloads

Enable the high-performance transfer backend:

```bash
pip install -U hf_transfer
HF_HUB_ENABLE_HF_TRANSFER=1 hf download winterForestStump/10-K_sec_filings \
  --repo-type dataset --local-dir ./data
```

On Windows PowerShell, set the env var separately:

```powershell
$env:HF_HUB_ENABLE_HF_TRANSFER = "1"
hf download winterForestStump/10-K_sec_filings --repo-type dataset --local-dir ./data
```

---

## Option 2 — Python with `datasets`

Install:

```bash
pip install -U datasets
```

Load the dataset (downloads and caches automatically):

```python
from datasets import load_dataset

# Load a single split to start (avoids pulling all ~13 GB at once)
ds = load_dataset("winterForestStump/10-K_sec_filings", split="001")
print(ds)
print(ds[0]["company_name"], ds[0]["filing_date"])
```

Load all splits:

```python
from datasets import load_dataset

ds = load_dataset("winterForestStump/10-K_sec_filings")  # DatasetDict with splits 001..052
print(ds.keys())
```

Stream without downloading everything (good for large iteration):

```python
from datasets import load_dataset

ds = load_dataset("winterForestStump/10-K_sec_filings", split="001", streaming=True)
for row in ds.take(5):
    print(row["company_name"])
```

---

## Option 3 — Python with `huggingface_hub` (raw files)

Download the parquet files directly without the `datasets` library:

```python
from huggingface_hub import snapshot_download

path = snapshot_download(
    repo_id="winterForestStump/10-K_sec_filings",
    repo_type="dataset",
    local_dir="./data",
    allow_patterns=["data/001-*", "data/002-*"],  # omit to download everything
)
print("Downloaded to:", path)
```

Then read with pandas / pyarrow:

```python
import pandas as pd

df = pd.read_parquet("./data/data/001-00000-of-00001-ecbd6ff05ee6eec2.parquet")
print(df.shape)
print(df.columns.tolist())
```

---

## Notes

- A Hugging Face account/token is **not required** for this public dataset, but if you
  hit rate limits run `hf auth login` (older: `huggingface-cli login`) first.
- By default `--local-dir` writes real files; the standalone Hub cache lives under
  `~/.cache/huggingface/hub` (`%USERPROFILE%\.cache\huggingface\hub` on Windows).
- The `data/` (and `datasets--*`) folders are git-ignored — see [.gitignore](.gitignore).
