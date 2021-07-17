import logging

import pandas as pd

logger = logging.getLogger("django.server")


def read_csv(filename):
    """
    Gets organization subscriptions
    Args:
        org_id: Organization Id
        type: active | inactive | None
            when active-> Returns active subscriptions
            when inactive-> Returns inactive subscriptions
            otherwise-> Returns all subscriptions
    """
    print("filename: ", filename)
    try:
        df = pd.read_csv(filename)
    except Exception as e:
        logger.error({"event_name": "CSV FORMAT IS NOT UTF-8", "error": str(e)})
        df = pd.read_csv(filename, encoding="latin-1", error_bad_lines=False)
    return df


def write_csv(filename, df):
    """
    Gets organization subscriptions
    Args:
        org_id: Organization Id
        type: active | inactive | None
            when active-> Returns active subscriptions
            when inactive-> Returns inactive subscriptions
            otherwise-> Returns all subscriptions
    """
    df.to_csv(filename, index=False)


def process_data(df):
    """
    Gets organization subscriptions
    Args:
        org_id: Organization Id
        type: active | inactive | None
            when active-> Returns active subscriptions
            when inactive-> Returns inactive subscriptions
            otherwise-> Returns all subscriptions
    """
    for idx, row in df.iterrows():
        print("index: ", idx, "Val: ", row["AudioType"])
        if idx == 10:
            break
