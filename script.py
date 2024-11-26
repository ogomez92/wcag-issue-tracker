import sys
import json
import os

ISSUES_FILE = 'issues.json'

WCAG_CRITERIA = {
    '1.1.1': 'Non-text Content',
    '1.2.1': 'Audio-only and Video-only (Prerecorded)',
    '1.2.2': 'Captions (Prerecorded)',
    '1.2.3': 'Audio Description or Media Alternative (Prerecorded)',
    '1.2.4': 'Captions (Live)',
    '1.2.5': 'Audio Description (Prerecorded)',
    '1.3.1': 'Info and Relationships',
    '1.3.2': 'Meaningful Sequence',
    '1.3.3': 'Sensory Characteristics',
    '1.3.4': 'Orientation',
    '1.3.5': 'Identify Input Purpose',
    '1.3.6': 'Identify Purpose',
    '1.4.1': 'Use of Color',
    '1.4.2': 'Audio Control',
    '1.4.3': 'Contrast (Minimum)',
    '1.4.4': 'Resize Text',
    '1.4.5': 'Images of Text',
    '1.4.6': 'Contrast (Enhanced)',
    '1.4.7': 'Low or No Background Audio',
    '1.4.8': 'Visual Presentation',
    '1.4.9': 'Images of Text (No Exception)',
    '1.4.10': 'Reflow',
    '1.4.11': 'Non-text Contrast',
    '1.4.12': 'Text Spacing',
    '1.4.13': 'Content on Hover or Focus',
    '2.1.1': 'Keyboard',
    '2.1.2': 'No Keyboard Trap',
    '2.1.3': 'Keyboard (No Exception)',
    '2.1.4': 'Character Key Shortcuts',
    '2.2.1': 'Timing Adjustable',
    '2.2.2': 'Pause, Stop, Hide',
    '2.2.3': 'No Timing',
    '2.2.4': 'Interruptions',
    '2.2.5': 'Re-authenticating',
    '2.2.6': 'Timeouts',
    '2.3.1': 'Three Flashes or Below Threshold',
    '2.3.2': 'Three Flashes',
    '2.3.3': 'Animation from Interactions',
    '2.4.1': 'Bypass Blocks',
    '2.4.2': 'Page Titled',
    '2.4.3': 'Focus Order',
    '2.4.4': 'Link Purpose (In Context)',
    '2.4.5': 'Multiple Ways',
    '2.4.6': 'Headings and Labels',
    '2.4.7': 'Focus Visible',
    '2.4.8': 'Location',
    '2.4.9': 'Link Purpose (Link Only)',
    '2.4.10': 'Section Headings',
    '2.5.1': 'Pointer Gestures',
    '2.5.2': 'Pointer Cancellation',
    '2.5.3': 'Label in Name',
    '2.5.4': 'Motion Actuation',
    '2.5.5': 'Target Size',
    '2.5.6': 'Concurrent Input Mechanisms',
    '3.1.1': 'Language of Page',
    '3.1.2': 'Language of Parts',
    '3.1.3': 'Unusual Words',
    '3.1.4': 'Abbreviations',
    '3.1.5': 'Reading Level',
    '3.1.6': 'Pronunciation',
    '3.2.1': 'On Focus',
    '3.2.2': 'On Input',
    '3.2.3': 'Consistent Navigation',
    '3.2.4': 'Consistent Identification',
    '3.2.5': 'Change on Request',
    '3.3.1': 'Error Identification',
    '3.3.2': 'Labels or Instructions',
    '3.3.3': 'Error Suggestion',
    '3.3.4': 'Error Prevention (Legal, Financial, Data)',
    '3.3.5': 'Help',
    '3.3.6': 'Error Prevention (All)',
    '4.1.1': 'Parsing',
    '4.1.2': 'Name, Role, Value',
    '4.1.3': 'Status Messages'
    # Add more criteria based on WCAG 2.2 specs as needed
}

def load_issues():
    if not os.path.exists(ISSUES_FILE):
        return {}
    with open(ISSUES_FILE, 'r') as file:
        return json.load(file)

def save_issues(issues):
    with open(ISSUES_FILE, 'w') as file:
        json.dump(issues, file, indent=4)

def add_issue(criteria_number):
    if criteria_number not in WCAG_CRITERIA:
        print(f"Error: Criteria {criteria_number} not valid.")
        return
    issues = load_issues()
    issues[criteria_number] = issues.get(criteria_number, 0) + 1
    issues["last"] = criteria_number
    save_issues(issues)
    criteria_text = WCAG_CRITERIA[criteria_number]
    
    print(f"Issue {criteria_number} ({criteria_text}) added.")

def remove_last():
    issues = load_issues()
    last = issues.get("last")
    if last is None:
        print("I didn't find the last issue you added :()")
        return
    issues[last] -= 1
    if issues[last] == 0:
        del issues[last]
        issues["last"] = None
    save_issues(issues)
    criteria_text = WCAG_CRITERIA[last]
    print(f"Issue {last} ({criteria_text}) removed.")    
    
    
def report_issues():
    issues = load_issues()
    issues.pop("last", None) # That last issue is for reference and shouldn't be counted.
    total_issues = sum(issues.values())
    
    if total_issues == 0:
        print("No issues found.")
        return
    
    print(f"total number of issues is {total_issues}")
    # Sort the issues by count in descending order
    sorted_issues = sorted(issues.items(), key=lambda item: item[1], reverse=True)

    print(f"{'WCAG Criterion':<10} {'Count':<10} {'Description'}")
    print("-" * 50)
    for criteria, count in sorted_issues:
        description = WCAG_CRITERIA.get(criteria, 'Unknown Criteria')
        percentage = (count / total_issues) * 100
        print(f"{criteria:<10} {count:<10} ({description}) ({percentage:.2f}%)")
    
def criteria_search(text):
    found = False
    for criteria, description in WCAG_CRITERIA.items():
        if text.lower() in description.lower():
            print(f"{criteria}: {description}")
            found = True
    if not found:
        print("No criteria found.")
    
def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <command> [<args>]")
        return

    command = sys.argv[1]
    if command == 'add':
        if len(sys.argv) != 3:
            print("Usage: script.py add <criteria_number>")
            return
        add_issue(sys.argv[2])
    elif command == 'report':
        report_issues()
    elif command == 'find':
        criteria_search(sys.argv[2])
    elif command == 'oops':
        remove_last()
    else:
        print("Unknown command.")

if __name__ == '__main__':
    main()