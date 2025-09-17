import re

class RegexOperations:
    def extract_emails(self,text):
        pattern = r'/b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-}+\.[A-Z|a-z]{2,}\b'
        return  re.findall(pattern,text)

    def validate_date(self,date_string):
        #validates if a string is a date in "YYYY-MM-DD" format.
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        return bool(re.match(pattern,date_string))

    def replace_word(self,text,old_word,new_word):
        pattern = r'\b + re.escape(old_word) + r'
        return resub(pattern,new_word,text)

    def split_by_non_alphanumeric(self,text):
        return re.split(r'[^a-zA-Z0-9] +', text)

    #Example
    if _name_ == "_main_":
        regex_ops = RegexOperations()

    #I.Extract email addresses
    text_with_emails = "contact us at [email protected]or [email protected] for support"
    emails = regex_ops.extract_emails(text_with_emails)
    print(f"Extracted emails :{emails}")

    #II. Validate a date
    date1 ="2023-10-26"
    date2 ="2023/10/26"
    print(f"'{date1}'is a valid date format: {regex_ops.validate_date(date1)}")
    print(f"'{date2}' is a valid date format: {regex_ops.validate_date(date2)}")

    #III.Replace a word
    original_string = "The quick brown fox jumps over the lazy fox."
    modified_string = regex_ops.replace_word(original_string,"fox","dog")
    print(f"Original string:"'{original_string}')
    print(f"Modified string: '{modified_string}')

    #IV.Split by non-alphanumeric characters
    complex_string = "Hello, world! This is a test. 123_abc."
    split_parts = regex_ops.split_by_non-alphanumeric(complex_string)
    print(f"Split parts :{split_parts}")