import re

def count_valid_emails(emails):
    if not emails:
        return 0
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    count = 0
    
    for email in emails:
        if re.match(pattern, email):
                count += 1
    
    return count