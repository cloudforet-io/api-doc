---
description:  
---
# Token

>  **Package : spaceone.api.identity.v1**

## Token

{% hint style="info" %}
**Token Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [issue](Token.md#issue)| [IssueTokenRequest](Token.md#issuetokenrequest) | [TokenInfo](Token.md#tokeninfo) |  |
| 2 | [refresh](Token.md#refresh)|[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| [TokenInfo](Token.md#tokeninfo) |  |

### issue
> **POST** /identity/v1/token/issue
>



| Type | Message |
| :--- | :--- |
| Request | [IssueTokenRequest](Token.md#issuetokenrequest) |
| Response |  [TokenInfo](Token.md#tokeninfo)  |



### refresh
> **POST** /identity/v1/token/refresh
>



| Type | Message |
| :--- | :--- |
| Request | [Empty] |
| Response |  [TokenInfo](Token.md#tokeninfo)  |





## Message

### IssueTokenRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | credentials |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 2 | domain_id |string |✅ ||

### TokenInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | access_token |string | ||
| 2 | refresh_token |string | ||
