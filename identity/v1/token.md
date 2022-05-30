---
description:  
---
# Token

>  **Package : spaceone.api.identity.v1**

## Token

{% hint style="info" %}
**Token Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**issue**](token.md#issue)|   [IssueTokenRequest](token.md#issuetokenrequest) |   [TokenInfo](token.md#tokeninfo) |  |
| [**refresh**](token.md#refresh)| [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|   [TokenInfo](token.md#tokeninfo) |  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">issue</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   IssueTokenRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   TokenInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">refresh</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">  google.protobuf.Empty </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   TokenInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
