---
description:  
---
# Token

>  **Package : spaceone.api.identity.v1**

## Token

{% hint style="info" %}
**Token Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**issue**](token.md#issue)|   [IssueTokenRequest](token.md#issuetokenrequest) |   [TokenInfo](token.md#tokeninfo) |  |
| [**refresh**](token.md#refresh)| [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|   [TokenInfo](token.md#tokeninfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**issue**](token.md#issue) </div> | <div style="width:200px; text-align:center;">    [IssueTokenRequest](token.md#issuetokenrequest)  </div> | <div style="width:200px; text-align:center;">   [TokenInfo](token.md#tokeninfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**refresh**](token.md#refresh) </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:200px; text-align:center;">   [TokenInfo](token.md#tokeninfo)  </div> | <div style="width:400px;">  </div> | 
 

 
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
