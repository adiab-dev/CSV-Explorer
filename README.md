# CSV Explorer

**A lightweight web application for exploring, analyzing, and visualizing CSV datasets.**

CSV Explorer allows users to upload CSV files, inspect their contents, filter and sort data, calculate statistics, and generate interactive visualizations — all through a simple web interface.

---

## Features

- None yet, just a draft

---

## Technology Stack

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| HTML5      | Application structure           |
| CSS3       | Styling and responsive design   |
| JavaScript | Frontend functionality          |
| Python     | CSV processing and calculations |
| Flask      | Backend and HTTP endpoints      |
| Chart.js   | Data visualization              |

---

## How It Works

CSV Explorer uses a frontend/backend architecture.

1. The user uploads a CSV file through the frontend.
2. JavaScript sends the file to the Flask backend.
3. Python processes the CSV data and calculates the requested statistics.
4. The backend returns the results to the frontend.
5. JavaScript displays the data in tables and interactive charts.

---

### Prerequisites

- Python 3.10 or later.
- pip (Python package manager).
- Git.

## Project Structure

```text
csv-explorer/
│
├── backend/
│   ├── main.py
│   └── csv_processor.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── main.js
│
├── screenshots/
│
├── README.md
└── DEVELOPMENT.md
```

## Development

For information about the development process, challenges, technical decisions, and lessons learned, see [DEVELOPMENT.md](DEVELOPMENT.md).
