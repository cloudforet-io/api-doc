---
description:  
---
# Server info

>  **Package : spaceone.api.core.v1**

## ServerInfo

{% hint style="info" %}
**ServerInfo Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [get_version](Server-info.md#get_version)|[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| [VersionInfo](Server-info.md#versioninfo) |  |

### get_version



| Type | Message |
| :--- | :--- |
| Request | [Empty] |
| Response |  [VersionInfo](Server-info.md#versioninfo)  |





## Message

### VersionInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | version |string | ||
