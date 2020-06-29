---
description:  
---
# Network policy

>  **Package : spaceone.api.inventory.v1**

## NetworkPolicy

{% hint style="info" %}
**NetworkPolicy Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Network-policy.md#create)| [CreateNetworkPolicyRequest](Network-policy.md#createnetworkpolicyrequest) | [NetworkPolicyInfo](Network-policy.md#networkpolicyinfo) |  |
| 2 | [update](Network-policy.md#update)| [UpdateNetworkPolicyRequest](Network-policy.md#updatenetworkpolicyrequest) | [NetworkPolicyInfo](Network-policy.md#networkpolicyinfo) |  |
| 3 | [pin_data](Network-policy.md#pin_data)| [PinNetworkPolicyDataRequest](Network-policy.md#pinnetworkpolicydatarequest) | [NetworkPolicyInfo](Network-policy.md#networkpolicyinfo) |  |
| 4 | [delete](Network-policy.md#delete)| [NetworkPolicyRequest](Network-policy.md#networkpolicyrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [get](Network-policy.md#get)| [GetNetworkPolicyRequest](Network-policy.md#getnetworkpolicyrequest) | [NetworkPolicyInfo](Network-policy.md#networkpolicyinfo) |  |
| 6 | [list](Network-policy.md#list)| [NetworkPolicyQuery](Network-policy.md#networkpolicyquery) | [NetworkPoliciesInfo](Network-policy.md#networkpoliciesinfo) |  |
| 7 | [stat](Network-policy.md#stat)| [NetworkPolicyStatQuery](Network-policy.md#networkpolicystatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /inventory/v1/network-policies
>



| Type | Message |
| :--- | :--- |
| Request | [CreateNetworkPolicyRequest](Network-policy.md#createnetworkpolicyrequest) |
| Response |  [NetworkPolicyInfo](Network-policy.md#networkpolicyinfo)  |



### update
> **PUT** /inventory/v1/network-policy/{network_policy_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateNetworkPolicyRequest](Network-policy.md#updatenetworkpolicyrequest) |
| Response |  [NetworkPolicyInfo](Network-policy.md#networkpolicyinfo)  |



### pin_data
> **PUT** /inventory/v1/network-policy/{network_policy_id}/pin-data
>



| Type | Message |
| :--- | :--- |
| Request | [PinNetworkPolicyDataRequest](Network-policy.md#pinnetworkpolicydatarequest) |
| Response |  [NetworkPolicyInfo](Network-policy.md#networkpolicyinfo)  |



### delete
> **DELETE** /inventory/v1/network-policy/{network_policy_id}
>



| Type | Message |
| :--- | :--- |
| Request | [NetworkPolicyRequest](Network-policy.md#networkpolicyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /inventory/v1/network-policy/{network_policy_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetNetworkPolicyRequest](Network-policy.md#getnetworkpolicyrequest) |
| Response |  [NetworkPolicyInfo](Network-policy.md#networkpolicyinfo)  |



### list
> **GET** /inventory/v1/network-policies
>
> **POST** /inventory/v1/network-policies/search




| Type | Message |
| :--- | :--- |
| Request | [NetworkPolicyQuery](Network-policy.md#networkpolicyquery) |
| Response |  [NetworkPoliciesInfo](Network-policy.md#networkpoliciesinfo)  |



### stat
> **POST** /inventory/v1/network-policies/stat
>



| Type | Message |
| :--- | :--- |
| Request | [NetworkPolicyStatQuery](Network-policy.md#networkpolicystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateNetworkPolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | routing_tables |[RoutingTable](Network-policy.md#routingtable) |❌ ||
| 3 | dns |string |❌ ||
| 4 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 6 | reference |[NetworkPolicyReference](Network-policy.md#networkpolicyreference) |❌ ||
| 7 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 8 | zone_id |string |✅ ||
| 9 | domain_id |string |✅ ||

### GetNetworkPolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_policy_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### NetworkPoliciesInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[NetworkPolicyInfo](Network-policy.md#networkpolicyinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### NetworkPolicyInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_policy_id |string | ||
| 2 | name |string | ||
| 3 | routing_tables |[RoutingTable](Network-policy.md#routingtable) | ||
| 4 | dns |string | ||
| 5 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 6 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 7 | reference |[NetworkPolicyReference](Network-policy.md#networkpolicyreference) | ||
| 8 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 9 | collection_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 10 | region_info |[RegionInfo](Network-policy.md#regioninfo) | ||
| 11 | zone_info |[ZoneInfo](Network-policy.md#zoneinfo) | ||
| 12 | domain_id |string | ||
| 13 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### NetworkPolicyQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | network_policy_id |string |❌ ||
| 3 | name |string |❌ ||
| 4 | zone_id |string |❌ ||
| 5 | region_id |string |❌ ||
| 6 | domain_id |string |✅ ||

### NetworkPolicyReference
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_id |string | ||
| 2 | external_link |string | ||

### NetworkPolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_policy_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### NetworkPolicyStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### PinNetworkPolicyDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_policy_id |string |✅ ||
| 2 | keys |string |✅ ||
| 3 | domain_id |string |✅ ||

### RoutingTable
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cidr |string | ||
| 2 | destination |string | ||
| 3 | interface |string | ||

### UpdateNetworkPolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_policy_id |string |✅ ||
| 2 | name |string |❌ ||
| 3 | routing_tables |[RoutingTable](Network-policy.md#routingtable) |❌ ||
| 4 | dns |string |❌ ||
| 5 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 6 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | reference |[NetworkPolicyReference](Network-policy.md#networkpolicyreference) |❌ ||
| 8 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 9 | domain_id |string |✅ ||
