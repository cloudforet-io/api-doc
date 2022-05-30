---
description:  
---
# Token

>  **Package : spaceone.api.identity.v1**

## Token

{% hint style="info" %}
**Token Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**issue**](token.md#issue)|   [IssueTokenRequest](token.md#issuetokenrequest) |   [TokenInfo](token.md#tokeninfo) |
| [**refresh**](token.md#refresh)| [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|   [TokenInfo](token.md#tokeninfo) | 
 

 
### issue
> **POST** /identity/v1/token/issue
>


| Type | Message |
| :--- | :--- |
| Request | [IssueTokenRequest](token.md#issuetokenrequest) |
| Response |  [TokenInfo](token.md#tokeninfo)  |
 
 

 
### refresh
> **POST** /identity/v1/token/refresh
>


| Type | Message |
| :--- | :--- |
| Request | [Empty] |
| Response |  [TokenInfo](token.md#tokeninfo)  |


## 

## Message

### IssueTokenRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_id |string|❌| |
| credentials |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| user_type |string|❌| |
| domain_id |string|✅| |

### TokenInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| access_token |string | |
| refresh_token |string | |
