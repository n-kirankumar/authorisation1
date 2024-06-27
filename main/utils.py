import re
from constants import VALID_COUNTRY_LIST, EXCLUDED_NUMBERS, VALID_GENDERS, VALID_BLOOD_GROUPS
from log import logger

def is_valid_mobile(mobile):
    """
    Validate if a given mobile number is valid.

    Args:
        mobile (int): The mobile number to validate.

    Returns:
        bool: True if the mobile number is valid, False otherwise.
    """
    if not isinstance(mobile, int):
        logger.error(f"Invalid mobile number type - {type(mobile)}")
        return False

    converted_str = str(mobile)
    mobile_num = int(converted_str[2:])

    if len(converted_str) != 12:
        logger.error(f"Invalid Mobile number length {len(converted_str)} and valid length is 12")
        return False

    if mobile_num in EXCLUDED_NUMBERS:
        logger.info(f"{mobile_num} is in the excluded list")
        return True

    if converted_str[:2] not in VALID_COUNTRY_LIST:
        logger.error(f"Invalid country code - {converted_str[:2]} valid country codes are {VALID_COUNTRY_LIST}")
        return False

    logger.info("Mobile verification is successful")
    return True

def is_valid_email(email):
    """
    Validate if a given email address is valid.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        logger.info("Email verification is successful")
        return True
    else:
        logger.error("Invalid email format")
        return False

def is_valid_gender(gender):
    """
    Validate if a given gender is valid.

    Args:
        gender (str): The gender to validate.

    Returns:
        bool: True if the gender is valid, False otherwise.
    """
    if gender in VALID_GENDERS:
        logger.info("Gender verification is successful")
        return True
    else:
        logger.error(f"Invalid gender - {gender}. Valid genders are {VALID_GENDERS}")
        return False

def is_valid_blood_group(blood_group):
    """
    Validate if a given blood group is valid.

    Args:
        blood_group (str): The blood group to validate.

    Returns:
        bool: True if the blood group is valid, False otherwise.
    """
    if blood_group in VALID_BLOOD_GROUPS:
        logger.info("Blood group verification is successful")
        return True
    else:
        logger.error(f"Invalid blood group - {blood_group}. Valid blood groups are {VALID_BLOOD_GROUPS}")
        return False

def is_valid_dob(dob):
    """
    Validate if a given date of birth (DOB) is valid.

    Args:
        dob (str): The date of birth in YYYY-MM-DD format to validate.

    Returns:
        bool: True if the DOB is valid, False otherwise.
    """
    try:
        if re.match(r'\d{4}-\d{2}-\d{2}', dob):
            logger.info("DOB verification is successful")
            return True
        else:
            logger.error("Invalid DOB format. Required format is YYYY-MM-DD")
            return False
    except Exception as e:
        logger.error(f"DOB validation error: {e}")
        return False
