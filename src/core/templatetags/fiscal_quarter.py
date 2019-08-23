from django.template.defaulttags import register


@register.filter
def fiscal(date):
    """Filter to calculate the fiscal quater a date falls in.

    Args:
        date (DateTime): The date to convert to fiscal quaters.

    Returns:
        number: The quater which the date falls in.
    """
    month = date.month
    return ((month - 1) // 3) + 1
