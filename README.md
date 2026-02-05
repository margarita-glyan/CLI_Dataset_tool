# Dataset Tool

CLI tool for scanning, organizing, and analyzing datasets with images and text.

---

## Install (local)

```bash
python3 -m pip install -e .
```

---

## Commands

### Help

```bash
dataset-tool --help
```

---

### Scan dataset

```bash
dataset-tool scan <path>
```

With duplicate detection:

```bash
dataset-tool scan --dupes <path>
```

---

### Organize files

```bash
dataset-tool organize <input_dir> <output_dir>
```

Creates:

```
output_dir/
 ├── images/
 ├── texts/
 └── unknown/
```

---

### Generate manifest (JSON)

```bash
dataset-tool manifest <input_dir> <output.json>
```

---

### Dataset statistics

```bash
dataset-tool stats <path>
```

---

### Verbose logging

```bash
dataset-tool --verbose scan <path>
```

---

## Tests

```bash
pytest
```
![CI](https://github.com/margarita-glyan/CLI_Dataset_tool/actions/workflows/ci.yml/badge.svg)

