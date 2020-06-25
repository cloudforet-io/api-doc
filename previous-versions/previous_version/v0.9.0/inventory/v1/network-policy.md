---
description: null
---

# Network Policy

> **Package : spaceone.api.inventory.v1**

## NetworkPolicy

{% hint style="info" %}
**NetworkPolicy Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](network-policy.md#create) | [CreateNetworkPolicyRequest](network-policy.md#createnetworkpolicyrequest) | [NetworkPolicyInfo](network-policy.md#networkpolicyinfo) |  |
| 2 | [update](network-policy.md#update) | [UpdateNetworkPolicyRequest](network-policy.md#updatenetworkpolicyrequest) | [NetworkPolicyInfo](network-policy.md#networkpolicyinfo) |  |
| 3 | [pin\_data](network-policy.md#pin_data) | [PinNetworkPolicyDataRequest](network-policy.md#pinnetworkpolicydatarequest) | [NetworkPolicyInfo](network-policy.md#networkpolicyinfo) |  |
| 4 | [delete](network-policy.md#delete) | [NetworkPolicyRequest](network-policy.md#networkpolicyrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 5 | [get](network-policy.md#get) | [GetNetworkPolicyRequest](network-policy.md#getnetworkpolicyrequest) | [NetworkPolicyInfo](network-policy.md#networkpolicyinfo) |  |
| 6 | [list](network-policy.md#list) | [NetworkPolicyQuery](network-policy.md#networkpolicyquery) | [NetworkPoliciesInfo](network-policy.md#networkpoliciesinfo) |  |
| 7 | [stat](network-policy.md#stat) | [NetworkPolicyStatQuery](network-policy.md#networkpolicystatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### create

> **POST** /inventory/v1/network-policies

| Type | Message |
| :--- | :--- |
| Request | [CreateNetworkPolicyRequest](network-policy.md#createnetworkpolicyrequest) |
| Response | [NetworkPolicyInfo](network-policy.md#networkpolicyinfo) |

### update

> **PUT** /inventory/v1/network-policy/{network\_policy\_id}

| Type | Message |
| :--- | :--- |
| Request | [UpdateNetworkPolicyRequest](network-policy.md#updatenetworkpolicyrequest) |
| Response | [NetworkPolicyInfo](network-policy.md#networkpolicyinfo) |

### pin\_data

> **PUT** /inventory/v1/network-policy/{network\_policy\_id}/pin-data

| Type | Message |
| :--- | :--- |
| Request | [PinNetworkPolicyDataRequest](network-policy.md#pinnetworkpolicydatarequest) |
| Response | [NetworkPolicyInfo](network-policy.md#networkpolicyinfo) |

### delete

> **DELETE** /inventory/v1/network-policy/{network\_policy\_id}

| Type | Message |
| :--- | :--- |
| Request | [NetworkPolicyRequest](network-policy.md#networkpolicyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /inventory/v1/network-policy/{network\_policy\_id}

| Type | Message |
| :--- | :--- |
| Request | [GetNetworkPolicyRequest](network-policy.md#getnetworkpolicyrequest) |
| Response | [NetworkPolicyInfo](network-policy.md#networkpolicyinfo) |

### list

> **GET** /inventory/v1/network-policies
>
> **POST** /inventory/v1/network-policies/search

| Type | Message |
| :--- | :--- |
| Request | [NetworkPolicyQuery](network-policy.md#networkpolicyquery) |
| Response | [NetworkPoliciesInfo](network-policy.md#networkpoliciesinfo) |

### stat

> **POST** /inventory/v1/network-policies/stat

| Type | Message |
| :--- | :--- |
| Request | [NetworkPolicyStatQuery](network-policy.md#networkpolicystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## Message

### CreateNetworkPolicyRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  | required |
| 2 | routing\_tables | [RoutingTable](network-policy.md#routingtable) |  | optional |
| 3 | dns | string |  | optional |
| 4 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 5 | metadata | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 6 | reference | [NetworkPolicyReference](network-policy.md#networkpolicyreference) |  | optional |
| 7 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 8 | zone\_id | string |  | required |
| 9 | domain\_id | string |  | required |

### GetNetworkPolicyRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network\_policy\_id | string |  | required |
| 2 | domain\_id | string |  | required |
| 3 | only | string |  | optional |

### NetworkPoliciesInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [NetworkPolicyInfo](network-policy.md#networkpolicyinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### NetworkPolicyInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network\_policy\_id | string |  |  |
| 2 | name | string |  |  |
| 3 | routing\_tables | [RoutingTable](network-policy.md#routingtable) |  |  |
| 4 | dns | string |  |  |
| 5 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 6 | metadata | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 7 | reference | [NetworkPolicyReference](network-policy.md#networkpolicyreference) |  |  |
| 8 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 9 | collection\_info | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 10 | region\_info | [RegionInfo](network-policy.md#regioninfo) |  |  |
| 11 | zone\_info | [ZoneInfo](network-policy.md#zoneinfo) |  |  |
| 12 | domain\_id | string |  |  |
| 13 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |

### NetworkPolicyQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |  | optional |
| 2 | network\_policy\_id | string |  | optional |
| 3 | name | string |  | optional |
| 4 | zone\_id | string |  | optional |
| 5 | region\_id | string |  | optional |
| 6 | domain\_id | string |  | required |

### NetworkPolicyReference

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource\_id | string |  |  |
| 2 | external\_link | string |  |  |

### NetworkPolicyRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network\_policy\_id | string |  | required |
| 2 | domain\_id | string |  | required |

### NetworkPolicyStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |  | required |
| 2 | domain\_id | string |  | required |

### PinNetworkPolicyDataRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network\_policy\_id | string |  | required |
| 2 | keys | string |  | required |
| 3 | domain\_id | string |  | required |

### RoutingTable

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cidr | string |  |  |
| 2 | destination | string |  |  |
| 3 | interface | string |  |  |

### UpdateNetworkPolicyRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network\_policy\_id | string |  | required |
| 2 | name | string |  | optional |
| 3 | routing\_tables | [RoutingTable](network-policy.md#routingtable) |  | optional |
| 4 | dns | string |  | optional |
| 5 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 6 | metadata | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 7 | reference | [NetworkPolicyReference](network-policy.md#networkpolicyreference) |  | optional |
| 8 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 9 | domain\_id | string |  | required |

