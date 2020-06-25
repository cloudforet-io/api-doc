---
description: null
---

# Policy

> **Package : spaceone.api.identity.v1**

## Policy

{% hint style="info" %}
**Policy Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](policy.md#create) | [CreatePolicyRequest](policy.md#createpolicyrequest) | [PolicyInfo](policy.md#policyinfo) |  |
| 2 | [update](policy.md#update) | [UpdatePolicyRequest](policy.md#updatepolicyrequest) | [PolicyInfo](policy.md#policyinfo) |  |
| 3 | [delete](policy.md#delete) | [PolicyRequest](policy.md#policyrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 4 | [get](policy.md#get) | [GetPolicyRequest](policy.md#getpolicyrequest) | [PolicyInfo](policy.md#policyinfo) |  |
| 5 | [list](policy.md#list) | [PolicyQuery](policy.md#policyquery) | [PoliciesInfo](policy.md#policiesinfo) |  |
| 6 | [stat](policy.md#stat) | [PolicyStatQuery](policy.md#policystatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### create

> **POST** /identity/v1/policies

| Type | Message |
| :--- | :--- |
| Request | [CreatePolicyRequest](policy.md#createpolicyrequest) |
| Response | [PolicyInfo](policy.md#policyinfo) |

### update

> **PUT** /identity/v1/policy/{policy\_id}

| Type | Message |
| :--- | :--- |
| Request | [UpdatePolicyRequest](policy.md#updatepolicyrequest) |
| Response | [PolicyInfo](policy.md#policyinfo) |

### delete

> **DELETE** /identity/v1/policy/{policy\_id}

| Type | Message |
| :--- | :--- |
| Request | [PolicyRequest](policy.md#policyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /identity/v1/policy/{policy\_id}

| Type | Message |
| :--- | :--- |
| Request | [GetPolicyRequest](policy.md#getpolicyrequest) |
| Response | [PolicyInfo](policy.md#policyinfo) |

### list

> **GET** /identity/v1/policies
>
> **POST** /identity/v1/policies/search

| Type | Message |
| :--- | :--- |
| Request | [PolicyQuery](policy.md#policyquery) |
| Response | [PoliciesInfo](policy.md#policiesinfo) |

### stat

> **POST** /identity/v1/policies/stat

| Type | Message |
| :--- | :--- |
| Request | [PolicyStatQuery](policy.md#policystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## Message

### CreatePolicyRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  | required |
| 2 | permissions | string |  | required |
| 3 | domain\_id | string |  | required |
| 4 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |

### GetPolicyRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | policy\_id | string |  | required |
| 2 | domain\_id | string |  | required |
| 3 | only | string |  | optional |

### PoliciesInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [PolicyInfo](policy.md#policyinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### PolicyInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | policy\_id | string |  |  |
| 2 | name | string |  |  |
| 3 | permissions | string |  |  |
| 4 | domain\_id | string |  |  |
| 5 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 6 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |

### PolicyQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |  | optional |
| 2 | policy\_id | string |  | optional |
| 3 | name | string |  | optional |
| 4 | domain\_id | string |  | required |

### PolicyRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | policy\_id | string |  | required |
| 2 | domain\_id | string |  | required |

### PolicyStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |  | required |
| 2 | domain\_id | string |  | required |

### UpdatePolicyRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | policy\_id | string |  | required |
| 2 | name | string |  | optional |
| 3 | permissions | string |  | optional |
| 4 | domain\_id | string |  | required |
| 5 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |

