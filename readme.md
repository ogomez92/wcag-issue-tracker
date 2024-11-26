# WCAG Issue Tracker

This script helps in tracking issues related to WCAG (Web Content Accessibility Guidelines) criteria. It supports adding issues, removing the last added issue, generating a report of current issues, and searching for criteria by description.

## Getting Started

### Installation

1. Clone this repository.

   ```bash
   git clone https://github.com/ogomez92/wcag-issue-tracker.git
   ```

2. Navigate to the project directory.

   ```bash
   cd wcag-issue-tracker
   ```

## Usage

Run the script with the following commands:

### Add an Issue

To add an issue for a specific WCAG criterion:

```bash
python script.py add <criteria_number>
```

For example:

```bash
python script.py add 1.1.1
```

### Report Issues

To generate and view a report of all added issues:

```bash
python script.py report
```

### Find Criteria

To search for criteria by a keyword in their description:

```bash
python script.py find <keyword>
```

For example:

```bash
python script.py find headings
```

### Remove Last Issue

To remove the last added issue:

```bash
python script.py oops
```

## Acknowledgments

- The WCAG criteria descriptions come from the WCAG 2.2 specifications. All contributions are welcome.
