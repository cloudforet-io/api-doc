---
description: null
---

# Server Info

> **Package : spaceone.api.core.v1**

## ServerInfo

{% hint style="info" %}
**ServerInfo Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [get\_version](server-info.md#get_version) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) | [VersionInfo](server-info.md#versioninfo) |  |

### get\_version

| Type | Message |
| :--- | :--- |
| Request | \[Empty\] |
| Response | [VersionInfo](server-info.md#versioninfo) |

## Message

### VersionInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | version | string |  |  |

