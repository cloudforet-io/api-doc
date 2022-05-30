---
description:  
---
# Policy

>  **Package : spaceone.api.identity.v1**

## Policy

{% hint style="info" %}
**Policy Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](policy.md#create)|   [CreatePolicyRequest](policy.md#createpolicyrequest) |   [PolicyInfo](policy.md#policyinfo) |  |
| [**update**](policy.md#update)|   [UpdatePolicyRequest](policy.md#updatepolicyrequest) |   [PolicyInfo](policy.md#policyinfo) |  |
| [**delete**](policy.md#delete)|   [PolicyRequest](policy.md#policyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](policy.md#get)|   [GetPolicyRequest](policy.md#getpolicyrequest) |   [PolicyInfo](policy.md#policyinfo) |  |
| [**list**](policy.md#list)|   [PolicyQuery](policy.md#policyquery) |   [PoliciesInfo](policy.md#policiesinfo) |  |
| [**stat**](policy.md#stat)|   [PolicyStatQuery](policy.md#policystatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](policy.md#create) </div> | <div style="width:200px; text-align:center;">    [CreatePolicyRequest](policy.md#createpolicyrequest)  </div> | <div style="width:200px; text-align:center;">   [PolicyInfo](policy.md#policyinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](policy.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdatePolicyRequest](policy.md#updatepolicyrequest)  </div> | <div style="width:200px; text-align:center;">   [PolicyInfo](policy.md#policyinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](policy.md#delete) </div> | <div style="width:200px; text-align:center;">    [PolicyRequest](policy.md#policyrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](policy.md#get) </div> | <div style="width:200px; text-align:center;">    [GetPolicyRequest](policy.md#getpolicyrequest)  </div> | <div style="width:200px; text-align:center;">   [PolicyInfo](policy.md#policyinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](policy.md#list) </div> | <div style="width:200px; text-align:center;">    [PolicyQuery](policy.md#policyquery)  </div> | <div style="width:200px; text-align:center;">   [PoliciesInfo](policy.md#policiesinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](policy.md#stat) </div> | <div style="width:200px; text-align:center;">    [PolicyStatQuery](policy.md#policystatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /identity/v1/policies
>


| Type | Message |
| :--- | :--- |
| Request | [CreatePolicyRequest](policy.md#createpolicyrequest) |
| Response |  [PolicyInfo](policy.md#policyinfo)  |
 
 

 
### update
> **PUT** /identity/v1/policy/{policy_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdatePolicyRequest](policy.md#updatepolicyrequest) |
| Response |  [PolicyInfo](policy.md#policyinfo)  |
 
 

 
### delete
> **DELETE** /identity/v1/policy/{policy_id}
>


| Type | Message |
| :--- | :--- |
| Request | [PolicyRequest](policy.md#policyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /identity/v1/policy/{policy_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetPolicyRequest](policy.md#getpolicyrequest) |
| Response |  [PolicyInfo](policy.md#policyinfo)  |
 
 

 
### list
> **GET** /identity/v1/policies
>
> **POST** /identity/v1/policies/search



| Type | Message |
| :--- | :--- |
| Request | [PolicyQuery](policy.md#policyquery) |
| Response |  [PoliciesInfo](policy.md#policiesinfo)  |
 
 

 
### stat
> **POST** /identity/v1/policies/stat
>


| Type | Message |
| :--- | :--- |
| Request | [PolicyStatQuery](policy.md#policystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreatePolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| permissions |list of string|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### GetPolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| policy_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### PoliciesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of PolicyInfo](policy.md#policyinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### PolicyInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| policy_id |string | |
| name |string | |
| permissions |list of string | |
| domain_id |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| created_at |string | |

### PolicyQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| policy_id |string|❌| |
| name |string|❌| |
| domain_id |string|❌| |

### PolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| policy_id |string|✅| |
| domain_id |string|✅| |

### PolicyStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### UpdatePolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| policy_id |string|✅| |
| name |string|❌| |
| permissions |list of string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
