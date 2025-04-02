# Filo-loading-effect

A lightweight Python implementation of loading bars with two different approaches: a custom console progress bar and a tqdm-based loading bar. This project provides simple yet effective ways to display progress in your command-line applications.

## Features

- Custom console progress bar with percentage display
- tqdm-based loading bar with enhanced features
- Easy to integrate into existing projects
- Customizable bar length and appearance
- Real-time progress updates

## Installation

1. Clone this repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. For the tqdm-based implementation, install the required dependency:
```bash
pip install tqdm
```

## Usage

### Custom Progress Bar

```python
from loading_bar import progress_bar

# Set progress to 80%
progress_bar(80)

# Or use it in a loop
for i in range(100):
    progress_bar(i)
    # Your processing code here
```

### tqdm-based Loading Bar

```python
from tqdm import tqdm

total = 100
with tqdm(total=total, desc='Loading', ncols=100) as pbar:
    # Update progress to 80%
    pbar.update(80)
```

## Project Structure

- `loading_bar.py`: Custom implementation of a progress bar
- `loading_bar_tqdm.py`: tqdm-based loading bar implementation

## Requirements

- Python 3.x
- tqdm (for tqdm-based implementation)

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.
