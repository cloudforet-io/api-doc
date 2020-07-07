---
description:  
---
# Policy

>  **Package : spaceone.api.repository.v1**

## Policy

{% hint style="info" %}
**Policy Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](policy.md#create)| [CreatePolicyRequest](policy.md#createpolicyrequest) | [PolicyInfo](policy.md#policyinfo) |  |
| 2 | [**update**](policy.md#update)| [UpdatePolicyRequest](policy.md#updatepolicyrequest) | [PolicyInfo](policy.md#policyinfo) |  |
| 3 | [**delete**](policy.md#delete)| [PolicyRequest](policy.md#policyrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](policy.md#get)| [GetRepositoryPolicyRequest](policy.md#getrepositorypolicyrequest) | [PolicyInfo](policy.md#policyinfo) |  |
| 5 | [**list**](policy.md#list)| [PolicyQuery](policy.md#policyquery) | [PoliciesInfo](policy.md#policiesinfo) |  |
| 6 | [**stat**](policy.md#stat)| [PolicyStatQuery](policy.md#policystatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 
 
 
 
### create
> **POST** /repository/v1/policies
>


| Type | Message |
| :--- | :--- |
| Request | [CreatePolicyRequest](policy.md#createpolicyrequest) |
| Response |  [PolicyInfo](policy.md#policyinfo)  |
 
 
 
 
 
### update
> **PUT** /repository/v1/policy/{policy}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdatePolicyRequest](policy.md#updatepolicyrequest) |
| Response |  [PolicyInfo](policy.md#policyinfo)  |
 
 
 
 
 
### delete
> **DELETE** /repository/v1/policy/{policy}
>


| Type | Message |
| :--- | :--- |
| Request | [PolicyRequest](policy.md#policyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 
 
 
 
### get
> **GET** /repository/v1/policies/{policy}
>


| Type | Message |
| :--- | :--- |
| Request | [GetRepositoryPolicyRequest](policy.md#getrepositorypolicyrequest) |
| Response |  [PolicyInfo](policy.md#policyinfo)  |
 
 
 
 
 
### list
> **GET** /repository/v1/policies
>
> **POST** /repository/v1/policies/search



| Type | Message |
| :--- | :--- |
| Request | [PolicyQuery](policy.md#policyquery) |
| Response |  [PoliciesInfo](policy.md#policiesinfo)  |
 
 
 
 
 
### stat
> **POST** /repository/v1/policies/stat
>


| Type | Message |
| :--- | :--- |
| Request | [PolicyStatQuery](policy.md#policystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreatePolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅||
| 2 | permissions |string|✅||
| 3 | labels |string|❌||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌||
| 5 | project_id |string|❌||
| 6 | domain_id |string|✅||

### GetRepositoryPolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | policy_id |string|✅||
| 2 | domain_id |string|✅||
| 3 | repository_id |string|❌||
| 4 | only |string|❌||

### PoliciesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[PolicyInfo](policy.md#policyinfo)||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)||

### PolicyInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | name |string||
| 2 | service_type |string||
| 3 | policy |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)||
| 4 | labels |string||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)||
| 6 | repository_info |[RepositoryInfo](policy.md#repositoryinfo)||
| 7 | project_id |string||
| 8 | domain_id |string||
| 9 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto)||

### PolicyQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌||
| 2 | policy_id |string|❌||
| 3 | name |string|❌||
| 4 | project_id |string|❌||
| 5 | repository_id |string|✅||
| 6 | domain_id |string|✅||

### PolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | policy_id |string|✅||
| 2 | domain_id |string|✅||

### PolicyStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅||
| 2 | repository_id |string|✅||
| 3 | domain_id |string|✅||

### UpdatePolicyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | policy_id |string|✅||
| 2 | name |string|❌||
| 3 | permissions |string|❌||
| 4 | labels |string|❌||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌||
| 6 | domain_id |string|✅||
