# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Account
    from ._models_py3 import AccountListResult
    from ._models_py3 import AccountProperties
    from ._models_py3 import AccountSku
    from ._models_py3 import AccountSkuListResult
    from ._models_py3 import ApiKeys
    from ._models_py3 import ApiProperties
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import CallRateLimit
    from ._models_py3 import CheckDomainAvailabilityParameter
    from ._models_py3 import CheckSkuAvailabilityParameter
    from ._models_py3 import CommitmentCost
    from ._models_py3 import CommitmentPeriod
    from ._models_py3 import CommitmentPlan
    from ._models_py3 import CommitmentPlanListResult
    from ._models_py3 import CommitmentPlanProperties
    from ._models_py3 import CommitmentQuota
    from ._models_py3 import CommitmentTier
    from ._models_py3 import CommitmentTierListResult
    from ._models_py3 import Deployment
    from ._models_py3 import DeploymentListResult
    from ._models_py3 import DeploymentModel
    from ._models_py3 import DeploymentProperties
    from ._models_py3 import DeploymentScaleSettings
    from ._models_py3 import DomainAvailability
    from ._models_py3 import Encryption
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import Identity
    from ._models_py3 import IpRule
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import MetricName
    from ._models_py3 import NetworkRuleSet
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionListResult
    from ._models_py3 import PrivateEndpointConnectionProperties
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkResourceProperties
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import ProxyResource
    from ._models_py3 import QuotaLimit
    from ._models_py3 import RegenerateKeyParameters
    from ._models_py3 import RequestMatchPattern
    from ._models_py3 import Resource
    from ._models_py3 import ResourceSku
    from ._models_py3 import ResourceSkuListResult
    from ._models_py3 import ResourceSkuRestrictionInfo
    from ._models_py3 import ResourceSkuRestrictions
    from ._models_py3 import Sku
    from ._models_py3 import SkuAvailability
    from ._models_py3 import SkuAvailabilityListResult
    from ._models_py3 import SkuCapability
    from ._models_py3 import SkuChangeInfo
    from ._models_py3 import SystemData
    from ._models_py3 import ThrottlingRule
    from ._models_py3 import Usage
    from ._models_py3 import UsageListResult
    from ._models_py3 import UserAssignedIdentity
    from ._models_py3 import UserOwnedStorage
    from ._models_py3 import VirtualNetworkRule
except (SyntaxError, ImportError):
    from ._models import Account  # type: ignore
    from ._models import AccountListResult  # type: ignore
    from ._models import AccountProperties  # type: ignore
    from ._models import AccountSku  # type: ignore
    from ._models import AccountSkuListResult  # type: ignore
    from ._models import ApiKeys  # type: ignore
    from ._models import ApiProperties  # type: ignore
    from ._models import AzureEntityResource  # type: ignore
    from ._models import CallRateLimit  # type: ignore
    from ._models import CheckDomainAvailabilityParameter  # type: ignore
    from ._models import CheckSkuAvailabilityParameter  # type: ignore
    from ._models import CommitmentCost  # type: ignore
    from ._models import CommitmentPeriod  # type: ignore
    from ._models import CommitmentPlan  # type: ignore
    from ._models import CommitmentPlanListResult  # type: ignore
    from ._models import CommitmentPlanProperties  # type: ignore
    from ._models import CommitmentQuota  # type: ignore
    from ._models import CommitmentTier  # type: ignore
    from ._models import CommitmentTierListResult  # type: ignore
    from ._models import Deployment  # type: ignore
    from ._models import DeploymentListResult  # type: ignore
    from ._models import DeploymentModel  # type: ignore
    from ._models import DeploymentProperties  # type: ignore
    from ._models import DeploymentScaleSettings  # type: ignore
    from ._models import DomainAvailability  # type: ignore
    from ._models import Encryption  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import IpRule  # type: ignore
    from ._models import KeyVaultProperties  # type: ignore
    from ._models import MetricName  # type: ignore
    from ._models import NetworkRuleSet  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import PrivateEndpoint  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionListResult  # type: ignore
    from ._models import PrivateEndpointConnectionProperties  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkResourceProperties  # type: ignore
    from ._models import PrivateLinkServiceConnectionState  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import QuotaLimit  # type: ignore
    from ._models import RegenerateKeyParameters  # type: ignore
    from ._models import RequestMatchPattern  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceSku  # type: ignore
    from ._models import ResourceSkuListResult  # type: ignore
    from ._models import ResourceSkuRestrictionInfo  # type: ignore
    from ._models import ResourceSkuRestrictions  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SkuAvailability  # type: ignore
    from ._models import SkuAvailabilityListResult  # type: ignore
    from ._models import SkuCapability  # type: ignore
    from ._models import SkuChangeInfo  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import ThrottlingRule  # type: ignore
    from ._models import Usage  # type: ignore
    from ._models import UsageListResult  # type: ignore
    from ._models import UserAssignedIdentity  # type: ignore
    from ._models import UserOwnedStorage  # type: ignore
    from ._models import VirtualNetworkRule  # type: ignore

from ._cognitive_services_management_client_enums import (
    ActionType,
    CreatedByType,
    DeploymentProvisioningState,
    DeploymentScaleType,
    HostingModel,
    KeyName,
    KeySource,
    NetworkRuleAction,
    Origin,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    ProvisioningState,
    PublicNetworkAccess,
    QuotaUsageStatus,
    ResourceIdentityType,
    ResourceSkuRestrictionsReasonCode,
    ResourceSkuRestrictionsType,
    SkuTier,
    UnitType,
)

__all__ = [
    'Account',
    'AccountListResult',
    'AccountProperties',
    'AccountSku',
    'AccountSkuListResult',
    'ApiKeys',
    'ApiProperties',
    'AzureEntityResource',
    'CallRateLimit',
    'CheckDomainAvailabilityParameter',
    'CheckSkuAvailabilityParameter',
    'CommitmentCost',
    'CommitmentPeriod',
    'CommitmentPlan',
    'CommitmentPlanListResult',
    'CommitmentPlanProperties',
    'CommitmentQuota',
    'CommitmentTier',
    'CommitmentTierListResult',
    'Deployment',
    'DeploymentListResult',
    'DeploymentModel',
    'DeploymentProperties',
    'DeploymentScaleSettings',
    'DomainAvailability',
    'Encryption',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'Identity',
    'IpRule',
    'KeyVaultProperties',
    'MetricName',
    'NetworkRuleSet',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResult',
    'PrivateEndpointConnectionProperties',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkResourceProperties',
    'PrivateLinkServiceConnectionState',
    'ProxyResource',
    'QuotaLimit',
    'RegenerateKeyParameters',
    'RequestMatchPattern',
    'Resource',
    'ResourceSku',
    'ResourceSkuListResult',
    'ResourceSkuRestrictionInfo',
    'ResourceSkuRestrictions',
    'Sku',
    'SkuAvailability',
    'SkuAvailabilityListResult',
    'SkuCapability',
    'SkuChangeInfo',
    'SystemData',
    'ThrottlingRule',
    'Usage',
    'UsageListResult',
    'UserAssignedIdentity',
    'UserOwnedStorage',
    'VirtualNetworkRule',
    'ActionType',
    'CreatedByType',
    'DeploymentProvisioningState',
    'DeploymentScaleType',
    'HostingModel',
    'KeyName',
    'KeySource',
    'NetworkRuleAction',
    'Origin',
    'PrivateEndpointConnectionProvisioningState',
    'PrivateEndpointServiceConnectionStatus',
    'ProvisioningState',
    'PublicNetworkAccess',
    'QuotaUsageStatus',
    'ResourceIdentityType',
    'ResourceSkuRestrictionsReasonCode',
    'ResourceSkuRestrictionsType',
    'SkuTier',
    'UnitType',
]
