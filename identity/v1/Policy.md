---
description:  
---
# Policy

>  **Package : spaceone.api.identity.v1**

## Policy

{% hint style="info" %}
**Policy Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Policy.md#create)| [CreatePolicyRequest](Policy.md#createpolicyrequest) | [PolicyInfo](Policy.md#policyinfo) |  |
| 2 | [update](Policy.md#update)| [UpdatePolicyRequest](Policy.md#updatepolicyrequest) | [PolicyInfo](Policy.md#policyinfo) |  |
| 3 | [delete](Policy.md#delete)| [PolicyRequest](Policy.md#policyrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Policy.md#get)| [GetPolicyRequest](Policy.md#getpolicyrequest) | [PolicyInfo](Policy.md#policyinfo) |  |
| 5 | [list](Policy.md#list)| [PolicyQuery](Policy.md#policyquery) | [PoliciesInfo](Policy.md#policiesinfo) |  |
| 6 | [stat](Policy.md#stat)| [PolicyStatQuery](Policy.md#policystatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /identity/v1/policies
>



| Type | Message |
| :--- | :--- |
| Request | [CreatePolicyRequest](Policy.md#createpolicyrequest) |
| Response |  [PolicyInfo](Policy.md#policyinfo)  |



### update
> **PUT** /identity/v1/policy/{policy_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdatePolicyRequest](Policy.md#updatepolicyrequest) |
| Response |  [PolicyInfo](Policy.md#policyinfo)  |



### delete
> **DELETE** /identity/v1/policy/{policy_id}
>



| Type | Message |
| :--- | :--- |
| Request | [PolicyRequest](Policy.md#policyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /identity/v1/policy/{policy_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetPolicyRequest](Policy.md#getpolicyrequest) |
| Response |  [PolicyInfo](Policy.md#policyinfo)  |



### list
> **GET** /identity/v1/policies
>
> **POST** /identity/v1/policies/search




| Type | Message |
| :--- | :--- |
| Request | [PolicyQuery](Policy.md#policyquery) |
| Response |  [PoliciesInfo](Policy.md#policiesinfo)  |



### stat
> **POST** /identity/v1/policies/stat
>



| Type | Message |
| :--- | :--- |
| Request | [PolicyStatQuery](Policy.md#policystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreatePolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | permissions |string |✅ ||
| 3 | domain_id |string |✅ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||

### GetPolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | policy_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### PoliciesInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[PolicyInfo](Policy.md#policyinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### PolicyInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | policy_id |string | ||
| 2 | name |string | ||
| 3 | permissions |string | ||
| 4 | domain_id |string | ||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 6 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### PolicyQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | policy_id |string |❌ ||
| 3 | name |string |❌ ||
| 4 | domain_id |string |✅ ||

### PolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | policy_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### PolicyStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### UpdatePolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | policy_id |string |✅ ||
| 2 | name |string |❌ ||
| 3 | permissions |string |❌ ||
| 4 | domain_id |string |✅ ||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
