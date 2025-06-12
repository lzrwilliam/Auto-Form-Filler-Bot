# ⚡ Auto Form Filler Bot

![Python 3](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)  
![Selenium](https://img.shields.io/badge/Selenium-Automation-green?logo=selenium)  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> **Automate any radio- and checkbox-only web form** by feeding your own JSON dataset—fill, submit, repeat.

---

## ✨ Key Features

- **JSON-driven**  
  Load an array of structured responses and drive every click from your data.

- **Smart element detection**  
  Finds options by visible label; if missing, falls back to the first available choice.

- **Auto-scroll & delays**  
  Scrolls into view and inserts small pauses to mimic human interaction and ensure stability.

- **Batch submissions**  
  Iterate through *all* JSON records, filling & submitting automatically.

---

## 🗂️ Project Layout

auto-form-filler/

├── auto_filler.py # Main Python + Selenium script

├── responses.json # Your array of form-response objects

└── README.md # This documentation


---

## 🛠️ How It Works

1. **Load JSON**  
   Reads `responses.json` into Python list of dictionaries.

2. **Navigate & Fill**  
   - For each key/value pair in a response:  
     - **Single choice** → click matching radio label  
     - **Multiple choice** → click each checkbox label  
   - If a label isn’t found, **automatically selects** the first visible option.

3. **Submit & Repeat**  
   After filling all fields, clicks the **Submit** button, then moves on to the next record.

4. **Graceful timing**  
   Built-in waits and scrolls prevent “too fast” or “element not clickable” errors.

---

## 📋 Example Response Schema

Each object in `responses.json` corresponds to one full submission:

```json
{
  "gender":     "Female",
  "age":        "18–24 years",
  "budget":     "1,000–2,500 lei",
  "frequency":  "Monthly",
  "brands":     ["Fast Fashion", "Second-hand"],
  "influences": ["Social Media", "Friends"],
  "ethics":     "Yes, if price is fair",
  "impulse":    "Rarely",
  "submit":     "Yes"
}
```



## 🚀 Installation & Setup

1. **Clone this repository**
2. **Install dependencies**
```bash
pip install selenium
```
3. Prepare your data

- Edit responses.json to include your survey answers.

- Ensure each value exactly matches the label text in your target form.

- Make sure each value matches the exact label text in your target form.

## 🏁 Usage
Run the script:

```bash
python auto_filler.py
```
**Step 1**: Opens Chrome and navigates to your form URL.

**Step 2**: Loads your array of responses from responses.json.

**Step 3**: For each entry:

-- Clicks radios and checkboxes per your JSON data.

-- Falls back to the first choice on a missing label.

-- Clicks the Submit button.

Step 4: Logs progress and moves to the next record until done.

Sample console output:

```bash
⚙️ Filling record 3/60...
✅ “Female” selected for gender
⚠️ “Rarely” not found—defaulting to first option
✅ Form #3 submitted
```

**⚙️ Configuration Tips**

Field Order Matters

JSON keys are processed in the order you list them. Mirror your form’s layout for best results.

Exact Label Matching

Copy-and-paste question labels and option texts directly from the form UI to prevent mismatches.

Adjust Delays

If you hit speed or timeout errors, tweak the time.sleep(0.4) in click_option_by_text().

**Error Handling**

Look for “⚠️ Option not found” warnings—those entries will use a fallback selection.



