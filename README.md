# Network Mood Detector

A Python-based script to visualize the status of network devices as a "mood" graph. This project helps you monitor network devices by pinging them and visualizing their online/offline status in a bar chart.

## Features

- Pings multiple IP addresses or hostnames to check their status.
- Generates a graph that visualises the network devices' availability.
- Easy-to-use Python script that outputs a mood-based graph for your network.
- Requires Python 3.x and Matplotlib.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/zakmohamud03/network-mood-detector.git
    ```

2. **Navigate to the project folder**:
    ```bash
    cd network-mood-detector
    ```

3. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

   If you're using **macOS/Linux**, use `pip3` instead:
    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

1. **Edit the `hosts.txt` file** to include the IP addresses or hostnames of the devices you want to ping. Each device should be listed on a new line.
   
2. **Run the Python script** to ping the devices and generate the graph:
    ```bash
    python mood_detector.py
    ```

   If you're using **macOS/Linux**, use `python3` instead:
    ```bash
    python3 mood_detector.py
    ```

3. The script will output a **bar graph** showing the status of each device. A `0` value indicates the device is offline, and a `1` value indicates the device is online.

## Expected Output

After running the script, you should see a bar chart pop-up, where:

- Each device is represented on the x-axis.
- The y-axis shows whether the device is online or offline.
- A green bar indicates the device is online, and a red bar indicates the device is offline.

## .gitignore

This project includes a `.gitignore` file to prevent uploading generated or system files, such as:

- `hosts.txt` (should not be tracked)
- Python cache files (`__pycache__/`, `*.pyc`, `*.pyo`, `*.pyd`)
- VS Code settings folder (`.vscode/`)
- OS-specific files (`.DS_Store`, `Thumbs.db`)

## License

This project is released under the MIT License.
MIT License 


Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.