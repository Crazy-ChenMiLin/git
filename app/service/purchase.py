from decimal import Decimal


# 采购订单金额上限（元）
MAX_ORDER_AMOUNT = Decimal("100000")


def calc_total(price, quantity):
    """计算含税总额"""
    return Decimal(str(price)) * Decimal(str(quantity))


def is_over_limit(amount):
    """是否超过采购上限"""
    return amount > Decimal("80000")


def format_amount(amount):
    return f"¥{amount:,.2f}"
