# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""Azure Cloud Mappings"""
from msrestazure import azure_cloud

from .._version import VERSION
from .exceptions import MsticpyAzureConfigError

__version__ = VERSION
__author__ = "Pete Bryan"

_CLOUD_MAPPING = {
    "global": azure_cloud.AZURE_PUBLIC_CLOUD,
    "usgov": azure_cloud.AZURE_US_GOV_CLOUD,
    "de": azure_cloud.AZURE_GERMAN_CLOUD,
    "cn": azure_cloud.AZURE_CHINA_CLOUD,
}

_CLOUD_ALIASES = {"public": "global", "gov": "usgov", "germany": "de", "china": "cn"}


def create_cloud_suf_dict(suffix: str) -> dict:
    """
    Get all the suffixes for a specific service in a cloud.

    Parameters
    ----------
    suffix : str
        The name of the suffix to get details for.

    Returns
    -------
    dict
        A dictionary of cloud names and suffixes.
    """
    return {
        cloud: getattr(msr_cloud.suffixes, suffix)
        for cloud, msr_cloud in _CLOUD_MAPPING.items()
    }


def create_cloud_ep_dict(endpoint: str) -> dict:
    """
    Return lookup dict for cloud endpoints.

    Parameters
    ----------
    endpoint : str
        The name of the endpoint to retreive for each cloud.

    Returns
    -------
    dict
        A dictionary of cloud names and endpoints.

    """
    return {
        cloud: getattr(msr_cloud.endpoints, endpoint)
        for cloud, msr_cloud in _CLOUD_MAPPING.items()
    }


def get_all_endpoints(cloud: str) -> dict:
    """
    Get a list of all the endpoints for an Azure cloud.

    Parameters
    ----------
    cloud : str
        The name of the Azure cloud to get endpoints for.

    Returns
    -------
    dict
        A dictionary of endpoints for the cloud.

    Raises
    ------
    MsticpyAzureConfigError
        If the cloud name is not valid.

    """
    if cloud in _CLOUD_ALIASES.keys():
        cloud = _CLOUD_ALIASES[cloud]
    try:
        endpoints = _CLOUD_MAPPING[cloud].endpoints
    except KeyError:
        raise MsticpyAzureConfigError(
            f"""{cloud} is not a valid Azure cloud name.
        Valid names are 'global', 'usgov', 'de', 'cn'"""
        )
    return endpoints


def get_all_suffixes(cloud: str) -> dict:
    """
    Get a list of all the suffixes for an Azure cloud.

    Parameters
    ----------
    cloud : str
        The name of the Azure cloud to get suffixes for.

    Returns
    -------
    dict
        A dictionary of suffixes for the cloud.

    Raises
    ------
    MsticpyAzureConfigError
        If the cloud name is not valid.

    """
    if cloud in _CLOUD_ALIASES.keys():
        cloud = _CLOUD_ALIASES[cloud]
    try:
        endpoints = _CLOUD_MAPPING[cloud].suffixes
    except KeyError:
        raise MsticpyAzureConfigError(
            f"""{cloud} is not a valid Azure cloud name.
        Valid names are 'global', 'usgov', 'de', 'cn'"""
        )
    return endpoints
