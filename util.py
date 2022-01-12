def verify_phone_number(phone_number):
    phone_number = phone_number.replace("-", "")

    for digit in phone_number:
        if not digit.isdigit():
            return False

    return len(phone_number) == 10


def verify_email_address(email):
    if "@" not in email:
        return False

    split_email = email.split("@")
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False

    if "." not in domain:
        return False

    split_domain = domain.split(".")

    for section in split_domain:
        if len(section) == 0:
            return False

    return True


def get_contact_by_name(first_name, last_name, contacts):
    for contact in contacts:
        if contact["first_name"] == first_name and contact["last_name"] == last_name:
            return contact

    return None
